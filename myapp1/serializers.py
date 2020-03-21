from rest_framework import serializers
from .models import IndianIndices,IndianIndices2,GlobalIndices,GlobalIndices2,BSE,BSE2,NSE,NSE2,Sensex,Nifty,FillAndDill_Cash,FillAndDill_SEBI,FillAndDill_Cash2,Fill_SEBI2

class IndianIndicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=IndianIndices
        fields=('index','price','change','change_percent')
class IndianIndices2Serializer(serializers.ModelSerializer):
    class Meta:
        model=IndianIndices2
        fields=('name','current_value','change','change_percent','open','high','low')
class GlobalIndicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalIndices
        fields=('index','price','change','change_percent')
class GlobalIndices2Serializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalIndices2
        fields=('name','current_value','change','change_percent','open','high','low','prev_close','five_day')
class BSESerializer(serializers.ModelSerializer):
    class Meta:
        model=BSE
        fields=('company','price','change','val')
class BSE2Serializer(serializers.ModelSerializer):
    class Meta:
        model=BSE2
        fields=('company_name','group','high','low','last_price','change_percent','value','five_day')
class NSESerializer(serializers.ModelSerializer):
    class Meta:
        model=NSE
        fields=('company','price','change','val')
class NSE2Serializer(serializers.ModelSerializer):
    class Meta:
        model=NSE2
        fields=('company_name','high','low','last_price','change_percent','value','five_day')
class SensexSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensex
        fields=('value','time')
class NiftySerializer(serializers.ModelSerializer):
    class Meta:
        model=Nifty
        fields=('value','time')
class FillAndDill_CashSerializer(serializers.ModelSerializer):
    class Meta:
        model=FillAndDill_Cash
        fields=('date','net_fill','net_dill')
class FillAndDill_SEBISerializer(serializers.ModelSerializer):
    class Meta:
        model=FillAndDill_SEBI
        fields=('date','equity','debt')
class FillAndDill_Cash2Serializer(serializers.ModelSerializer):
    class Meta:
        model=FillAndDill_Cash2
        fields=('date','fill_gross_pur','fill_gross_sal','fill_net_pur','dill_gross_pur','dill_gross_sal','dill_net_pur')
class Fill_SEBI2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Fill_SEBI2
        fields=('date','equity_gross_pur','equity_gross_sal','equity_net_pur','debt_gross_pur','debt_gross_sal','debt_net_pur')
