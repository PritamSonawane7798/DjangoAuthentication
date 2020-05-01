from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import datetime
import os

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    message = "{} server is live current time is ".format(os.environ.get('ENV_VAR') )
    return Response(data=message + date,status=status.HTTP_200_OK)


