from django.shortcuts import render
from models import *


def home(request):
    return render(request, "home.html", {"table": Transaction.objects.all()})


def add(request):
    try:
        t = Transaction(id=request.GET["id"], name=request.GET["name"], bill=request.GET["bill"], datetime=request.GET["datetime"])
        t.save()
    except:
        ()

    # Transaction.objects.all().map_reduce()

    return render(request, "home.html", {"table": Transaction.objects.all()})


def delete(request):
    t = Transaction.objects.filter(id=request.GET["id"])
    t.delete()
    # t.save()

    return render(request, "home.html", {"table": Transaction.objects.all()})


def change(request):
    if request.GET["what"] == "name":
        Transaction.objects.filter(id=request.GET["id"]).update(name=request.GET["new"])
    elif request.GET["what"] == "bill":
        Transaction.objects.filter(id=request.GET["id"]).update(bill=request.GET["new"])
    elif request.GET["what"] == "datetime":
        Transaction.objects.filter(id=request.GET["id"]).update(datetime=request.GET["new"])

    return render(request, "home.html", {"table": Transaction.objects.all()})


def map_reduce_tests(request):
    map1 = """
    function() {
        emit(this.name, 1)
    }
    """

    reduce1 = """
    function reduce(key, values) {
      return values.length; /* == sum(values) */
    }
    """

    map2 = """
    function map() {
      /* `this` refers to the current document */
        emit(this.datetime, 1);
    } """

    reduce2 = """
    function reduce(key, values) {
      return values.length; /* == sum(values) */
    }
    """

    return render(request, "map_reduce_tests.html", {"table": Transaction.objects.all(), "map_reduce1": Transaction.objects.map_reduce(map1, reduce1, out='Test 1'), "map_reduce2": Transaction.objects.map_reduce(map2, reduce2, out='Test 2')})