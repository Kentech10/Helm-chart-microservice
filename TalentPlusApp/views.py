# import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
# import local data
from .serializers import TalentPlusSerializer
from .models import TalentPlus
from rest_framework.views import APIView

# create a viewset
class TalentPlusViewSet(viewsets.ModelViewSet):
    # specify serializer to be used
    serializer_class = TalentPlusSerializer

    # define queryset
    queryset = TalentPlus.objects.all()
    
    
    

    



    