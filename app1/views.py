from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import ProductSerializer

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
