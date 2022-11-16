#import serializer from rest_framework
from rest_framework import serializers
from .models import TalentPlus



# create a serializer
class TalentPlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentPlus
        fields = ("title", "discription")
    
    


   


