import os.path
from django.shortcuts import HttpResponse
from shop.models import Product
from shop import ProductSerializer as ps
import simplejson
from django.views.decorators.csrf import csrf_exempt

UPLOAD_DIR = os.path.dirname(__file__) + '/static/images/'

def list(request):
    try:
        product_name = request.GET["product_name"]
    except:
        product_name = ""
    items = Product.objects.filter(product_name__contains=product_name).order_by("-product_name")
#             테이블 레코드 정렬        (-)내림
    serializer = ps.ProductSerializer(items, many=True)
#       데이터 => 직렬화

    return HttpResponse(simplejson.dumps(serializer.data))
#                               json으로 변환

@csrf_exempt    # csrf 체크 면제
def insert(request):
    if "img" in request.FILES:
        file = request.FILES["img"]
        file_name = file._name
        fp = open("%s%s" % (UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
#                          첨부파일 조각
            fp.write(chunk)
        fp.close()
    else:
        file_name = "-"
    row = Product(product_name=request.POST["product_name"], description=request.POST["description"],
                  price=request.POST["price"], filename=file_name)
    row.save()

def detail(request, product_code):
    row = Product.objects.get(product_code=product_code)
    serializer = ps.ProductSerializer(row)
    return HttpResponse(simplejson.dumps(serializer.data))