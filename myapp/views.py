from django.shortcuts import render, HttpResponse, redirect
from .models import *
from math import ceil
from json import *
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_KEY = "OApSZhsAutey7TDE"


def index(request):
    Largedata = []
    nosildes = 0
    l = []
    cate = []
    allproducts = productdetails.objects.values("category")
    for items in allproducts:
        if items != 0:
            cate.append(items["category"])
    cats = set(cate)
    for cat in cats:
        d = productdetails.objects.filter(category=cat)
        data = d
        n = len(data)
        no = n // 4 + ceil(n / 4 - n // 4)
        nosildes = no
        Largedata.append([data, range(1, nosildes), nosildes])
    Information = {"allproducts": Largedata}
    return render(request, "Shops\Index.html", Information)


def about(request):
    return render(request, "Shops/about.html")


def Cont(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        Phone_no = request.POST["phone"]
        Query = request.POST["desc"]
        data = Contact(name=name, email=email, Phoneno=Phone_no, desc=Query)
        data.save()
        thank = True
        return render(request, "Shops/Contact.html", {"thank": thank})
    return render(request, "Shops/Contact.html")


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get("orderId", "")
        email = request.POST.get("email", "")
        try:
            order = Orders.objects.filter(O_id=orderId, Email_id=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {"text": item.update_desc, "time": item.timeStamp})
                    response = dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request, "Shops/Tracker.html")


def search(request):
    if request.POST:
        data = request.POST["Search"]
        getdata = productdetails.objects.filter(category__icontains=data)
        n = len(getdata)
        noslides = n // 4 + ceil(n / 4 - n // 4)
        largdata = []
        largdata.append([getdata, range(1, noslides), noslides])
    d1 = {"information": largdata}
    return render(request, "Shops/Search.html", d1)


def productView(request, myid):
    Maindata = productdetails.objects.filter(id=myid)
    product = {"data": Maindata}
    return render(request, "Shops/productdetails.html", product)


def Checkout(request):
    if request.POST:
        try:
            Name = request.POST["name"]
            Email = request.POST["Email"]
            Address = (
                request.POST.get("Address", "") + " " +
                request.POST.get("Address2", "")
            )
            item_Json = request.POST.get("itemsJson")
            amount = request.POST.get("amount")
            State = request.POST["State"]
            City = request.POST["City"]
            Zip_name = request.POST["Zip"]
            Phone_number = request.POST["iPhone"]
            orde = Orders(
                Name=Name,
                Email_id=Email,
                Address=Address,
                City=City,
                State=State,
                Zip_code=Zip_name,
                Phone_number=Phone_number,
                item_Json=item_Json,
                Amount=int(amount),
            )
            orde.save()
            thank = True
            id = orde.O_id
            data = OrderUpdate(order_id=orde.O_id,
                               update_desc="Your order has been placed")
            data.save()
            param_dict = {
                "MID": "OnSvFk39657322013849",
                "ORDER_ID": str(orde.O_id),
                "TXN_AMOUNT": str(amount),
                "CUST_ID": Email,
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CHANNEL_ID": "WEB",
                "CALLBACK_URL": "http://127.0.0.1:8000/shop/handelrequest/",
            }
            param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(
                param_dict, MERCHANT_KEY
            )
        except Exception as p:
            return HttpResponse('<h1>Select any Item to cart</h1><br><a href="/shop" style="color:red;background-color:blue;"><button>Go back</button></a>')
        return render(request, "Shops/Paytm.html", {"param_dict": param_dict})
    return render(request, "Shops/Checkout.html")


@csrf_exempt
def handelRequest(request):
    return render(request, "Shops/SuccessPayment.html")
