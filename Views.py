import random

from django.shortcuts import *
from django.http import *
from pymysql import *
from django.views.decorators.csrf import *
from django.core.files.storage import *

conn = Connect("127.0.0.1", "root", "", "goodreads")


def loginpage(request):
    return render(request, "login.html")


def login(request):
    global conn
    email = request.GET["Email"]
    Password = request.GET["Password"]
    s = "select* from admin1 where Email='" + email + "' and Password='" + Password + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        request.session['e'] = email
        return render(request, "admindashboard.html")
    else:
        d = {"message": "invalid credentials"}
    return render(request, "login.html", {"ar": d})


def addadmin(request):
    return render(request, "addadmin.html")


# @csrf_exempt
# def insertadmin(request):
# conn=Connect("127.0.0.1","root","","goodreads")
#     s="insert into  admin1 values('"+request.POST["Email"]+"','"+request.POST["Password"]+"','"+request.POST["Mobileno"]+"',0)"
#     cr=conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     d={"message":"admin added successfully"}
#     return render(request, "insertadmin.html", {"ar":d})
# @csrf_exempt
# def showadmin(request):
#     conn=Connect("127.0.0.1","root","","goodreads")
#     s="select* from admin1"
#     cr=conn.cursor()
#     cr.execute(s)
#     result=cr.fetchall()
#     x=[]
#     for row in result:
#         d={}
#         d["Email"]=row[0]
#         d["Password"]=row[1]
#         d["Mobileno"]=row[2]
#         d["otp"]=row[3]
#         x.append(d)
#     return render(request, "showadmin.html", {"ar": x})
@csrf_exempt
def changepassword(request):
    return render(request, "changepassword.html")


@csrf_exempt
def updatepassword(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    email = str(request.session['e'])
    s = "select * from admin1 where Email='" + email + "' and Password='" + request.POST["oldpassword"] + "'"
    print("hello")
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    if result:
        s = "update admin1 set Password='" + request.POST["newpassword"] + "' where Email='" + email + "'"
        print("Bye")
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        d = {"message": "password changed successfully"}
        return render(request, "admindashboard.html", {"ar": d})
    else:

        d = {"message": "invalid credentials"}
        return render(request, "changepassword.html", {"ar": d})


def insertadmin(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")

    s = "insert into admin1 values('" + request.GET["Email"] + "','" + request.GET["Password"] + "','" + request.GET[
        "Mobileno"] + "',0)"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "Admin added successfully"}
    return render(request, "insertadmin.html", {"ar": d})


def showadmin(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from admin1"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {}
        d["Email"] = row[0]
        d["Password"] = row[1]
        d["Mobileno"] = row[2]
        d["otp"] = row[3]
        x.append(d)
    return render(request, "showadmin.html", {"ar": x})


def removeadmin(request):
    conn = Connect("127.0.0.1", "root", "", "Goodreads")
    s = "delete from admin1 where Email='" + request.GET["q"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect("showadmin")


def editadmin(request):
    return render(request, "editadmin.html")


def save(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "update admin1 set Mobileno='" + request.GET["Mobileno"] + "' where Email='" + request.GET["Email"] + "'"
    # s="update admin1 set otp='"+request.GET["otp"]+"' where Email='"+request.GET["Email"]+"'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect("showadmin")


def editadmin(request):
    Email = request.GET["q"]
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from admin1 where Email='" + Email + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    result = cr.fetchone()
    d = {"Email": result[0], "Password": result[1], "Mobileno": result[2], "otp": result[3]}
    return render(request, "editadmin.html", {"ar": d})


def addcategory(request):
    return render(request, "addcategory.html")


@csrf_exempt
def insertcategory(request):
    file = request.FILES["photo"]
    print(file)
    uploadname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    fs = FileSystemStorage()
    fs.save(uploadname, file)
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "insert into category values('" + request.POST["catname"] + "','" + request.POST[
        "description"] + "','" + uploadname + "')"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "category added successfully"}
    return render(request, "insertcategory.html", {"ar": d})


def showcategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"catname": row[0], "description": row[1], "catphoto": row[2]}
        x.append(d)
    return render(request, "showcategory.html", {"ar": x})


def removecategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "delete from category where catname='" + request.GET["q"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect("showcategory")


def editcategory(request):
    return render(request, "editcategory.html")


@csrf_exempt
def save(request):
    try:
        file = request.FILES["photo"]

    except:
        file = ""

    if file != "":

        print(f"if condition{file}")
        file = request.FILES["photo"]
        uploadname = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
        s = "update category set description='" + request.POST[
            "description"] + "',catphoto='" + uploadname + "' where catname='" + request.POST["catname"] + "'"
        fs = FileSystemStorage()
        fs.save(uploadname, file)
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
    else:

        print(f"else condition:-{file}")
        s1 = "update category set description='" + request.POST["description"] + "' where catname='" + request.POST[
            "catname"] + "'"
        cr = conn.cursor()
        cr.execute(s1)
        conn.commit()

    return HttpResponseRedirect("showcategory")


def editcategory(request):
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "select * from category where catname='" + request.GET["q"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    result = cr.fetchone()
    d = {"catname": result[0], "description": result[1], "catphoto": result[2]}
    return render(request, "editcategory.html", {"ar": d})


def addbook(request):
    global conn
    s = " select catname from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)
    x = []
    for i in result:
        x.append(i[0])
    return render(request, "addbook.html", {"ar": x})


@csrf_exempt
def insertbook(request):
    file = request.FILES["photo"]
    print(file)
    name = ("categoryphotos/" + str(random.randint(1, 10000)) + file.name)
    conn = Connect("127.0.0.1", "root", "", "goodreads")
    s = "insert into books values(NULL,'" + request.POST["title"] + "','" + request.POST["description"] + "'," + \
        request.POST["price"] + ",'" + request.POST["edition"] + "','" + request.POST["author"] + "','" + request.POST[
            "genre"] + "','" + request.POST["catname"] + "','" + name + "')"
    fs = FileSystemStorage()
    fs.save(name, file)
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    d = {"message": "book added successfully"}
    return render(request, "insertbook.html", {"ar": d})


# def openajax(request):
#         return render(request,"ajaxdemo.html")
#
# def showbook(request):
#     global conn
#     cr = conn.cursor()
#     s="select catname from category"
#     cr.execute(s)
#     result = cr.fetchall()
#     x=[]
#     for row in result:
#         d={"catname":row[0]}
#         x.append(d)
#     return render(request,"ajaxdemo.html",{"ar":x})
#
# def getbooks(request):
#     global conn
#     catname=request.GET["catname"]
#     print(catname)
#     s="select * from books where catname='"+catname+"'"
#     print('')
#     cr=conn.cursor()
#     cr.execute(s)
#     result=cr.fetchall()
#     x=[]
#     for row in result:
#         d={"bookid":row[0],
#            "title":row[1],
#            "description":row[2],
#            "price":row[3],
#            "edition":row[4],
#            "author":row[5],
#            "genre":row[6],
#            "catname":row[7],
#            "photo":row[8]}
#         x.append(d)
#     print(x)
#     return JsonResponse(x,safe=False)
# def deleteaction(request):
#     id=request.GET["id"]
#     print(id)
#     s="delete from books where bookid=('{id}')"
#     print(s)
#     global conn
#     cr=conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     return HttpResponse("SUCCESS")
# @csrf_exempt
# def editdataaction(request):
#     bookid=request.POST['bookid']
#     title=request.POST['title']
#     description=request.POST['description']
#     price=request.POST['price']
#     edition=request.POST['edition']
#     author=request.POST['author']
#     genre=request.POST['genre']
#     catname=request.POST['catname']
#     photo=request.POST['photo']
#     s=f"update books set title='{title}',description=('{description}'),price='{price}',edition='{edition}',author='{author}',genre='{genre}',catname='{catname}',photo='{photo}' where bookid=('{bookid}')"
#     print(s)
#     global conn
#     cr=conn.cursor()
#     cr.execute(s)
#     conn.commit()
#     return HttpResponse("SUCCESS")
#
# #def changepassword(request):
#    # return render(request,"changepassword")
#
#
# def showbook2(request):
#     global conn
#     s = " select catname from category"
#     cr = conn.cursor()
#     cr.execute(s)
#     result = cr.fetchall()
#     print(result)
#     x=[]
#     for row in result:
#         d={"catname":row[0]}
#         x.append(d)
#     return render(request,"addbook.html",{"ar".x})
from database import *


def booksview(request):
    query = "select catname from category"
    result = Fetchall(query)
    x = []
    for i in result:
        x.append(i[0])
    return render(request, 'books.html', {"data": x})


def viewbooks(request):
    catname = request.GET['catname']
    query = f"select * from books where catname='{catname}'"

    result = Fetchall(query)
    x = []
    for row in result:
        disct = {}
        disct['id'] = row[0]
        disct['title'] = row[1]
        disct['description'] = row[2]
        disct['price'] = row[3]
        disct['edition'] = row[4]
        disct['author'] = row[5]
        disct['genre'] = row[6]
        disct['category'] = row[7]
        disct['photo'] = row[8]
        x.append(disct)
        data = {"x": x}
    return JsonResponse(data, safe=False)
def deltebooks(request):
    id = request.GET['id']
    query = f"delete from books where bookid={id}"
    result = Delete(query)
    return HttpResponse(result)

def editbook(request):
    id = request.GET['id']
    print(id)
    sql = "select * from books where bookid={id}"
    result = Update(sql)
    d=[]
    for i in result:
      d.append(i)
    return JsonResponse(d,safe=False)