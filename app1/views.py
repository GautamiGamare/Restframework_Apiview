from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import ProductSerializer
from app1.models import ProductModel

class showIndex(APIView):
    def get(self,request):
        d1 = {'id':101,'name':'Gautami','salary':25000}
        return Response(d1)

class productOperations(APIView):
    def post(self,request):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            msg = {'msg':'data is saved'}
        else:
            msg = {'error':ps.errors}
        return Response(msg)

    def get(self,request):
        qs = ProductModel.objects.all()
        ps = ProductSerializer(qs,many=True)
        return Response(ps.data)

class for_one_product(APIView):
    def get(self,request,pid):
        try:
            qs= ProductModel.objects.get(pid=pid)
            ps = ProductSerializer(qs)
            return Response(ps.data)
        except ProductModel.DoesNotExist:
            msg={'error':'Product Does not exist'}
            return Response(msg)

    def put(self,request,pid):
        try:
            qs = ProductModel.objects.get(pid=pid)
            data = request.data
            ps = ProductSerializer(qs,data,partial=True)
            if ps.is_valid():
                ps.save()
                msg = {'data':'data is saved'}
            else:
                msg = {'error':ps.errors}
            return Response(msg)
        except ProductModel.DoesNotExist:
            msg = {'data':'Product Doest not exist'}
            return (msg)

    def delete(self,request,pid):
        res = ProductModel.objects.filter(pid=pid).delete()
        if res[0]!=0:
            msg = {'data':'Product is deleted'}
        else:
            msg = {'error':'Invalid Product'}
        return Response(msg)
