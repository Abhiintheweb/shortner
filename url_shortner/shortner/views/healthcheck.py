from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


class HealthCheckView(APIView):

    def get(self, request):
        currentTime = datetime.now()
        return Response({'data': f'Up And Running at {currentTime}'})
