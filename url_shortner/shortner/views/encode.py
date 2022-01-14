from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from shortner.serializers.encode import EncodeSerializer


class EncodeView(APIView):

    def post(self, request):
        serializer = EncodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        return Response(data=serializer.data)
