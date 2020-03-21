from django.db import models

# Create your models here.
#indian indices
class IndianIndices(models.Model):
    index=models.CharField(max_length=30)
    price=models.FloatField(max_length=30)
    change=models.FloatField(max_length=30)
    change_percent=models.FloatField(max_length=30)

class IndianIndices2(models.Model):
    name=models.CharField(max_length=30)
    current_value=models.FloatField(max_length=30)
    change=models.FloatField(max_length=30)
    change_percent=models.FloatField(max_length=30)
    open=models.FloatField(max_length=30)
    high=models.FloatField(max_length=30)
    low=models.FloatField(max_length=30)

#global indices
class GlobalIndices(models.Model):
    index=models.CharField(max_length=30)
    price=models.FloatField(max_length=30)
    change=models.FloatField(max_length=30)
    change_percent=models.FloatField(max_length=30)

class GlobalIndices2(models.Model):
    name=models.CharField(max_length=30,null=True)
    current_value=models.FloatField(max_length=30,null=True)
    change=models.FloatField(max_length=30,null=True)
    change_percent=models.FloatField(max_length=30,null=True)
    open=models.FloatField(max_length=30,null=True)
    high=models.FloatField(max_length=30,null=True)
    low=models.FloatField(max_length=30,null=True)
    prev_close=models.FloatField(max_length=30,null=True)
    five_day=models.CharField(max_length=30,null=True)

#BSE
class BSE(models.Model):
    company=models.CharField(max_length=30)
    price=models.FloatField(max_length=30)
    change=models.FloatField(max_length=30)
    val=models.FloatField(max_length=30)

class BSE2(models.Model):
    company_name=models.CharField(max_length=30)
    group=models.CharField(max_length=30)
    high=models.FloatField(max_length=30)
    low=models.FloatField(max_length=30)
    last_price=models.FloatField(max_length=30)
    change_percent=models.FloatField(max_length=30)
    value=models.FloatField(max_length=30)
    five_day=models.CharField(max_length=30)

#NSE
class NSE(models.Model):
    company=models.CharField(max_length=30)
    price=models.FloatField(max_length=30)
    change=models.FloatField(max_length=30)
    val=models.FloatField(max_length=30)

class NSE2(models.Model):
    company_name=models.CharField(max_length=30)
    high=models.FloatField(max_length=30)
    low=models.FloatField(max_length=30)
    last_price=models.FloatField(max_length=30)
    change_percent=models.FloatField(max_length=30)
    value=models.FloatField(max_length=30)
    five_day=models.CharField(max_length=30)

#sensex and nifty
class Sensex(models.Model):
    value=models.IntegerField()
    time=models.TimeField(auto_now=False)

class Nifty(models.Model):
    value=models.IntegerField()
    time=models.TimeField(auto_now=False)

#fill dill activity(cash and fill SEBI)
class FillAndDill_Cash(models.Model):
    date=models.DateField()
    net_fill=models.FloatField(max_length=30)
    net_dill=models.FloatField(max_length=30)

class FillAndDill_SEBI(models.Model):
    date=models.DateField()
    equity=models.FloatField(max_length=30)
    debt=models.FloatField(max_length=30)

class FillAndDill_Cash2(models.Model):
    date=models.CharField(max_length=30)
    fill_gross_pur=models.FloatField(max_length=30)
    fill_gross_sal=models.FloatField(max_length=30)
    fill_net_pur=models.FloatField(max_length=30)
    dill_gross_pur=models.FloatField(max_length=30)
    dill_gross_sal=models.FloatField(max_length=30)
    dill_net_pur=models.FloatField(max_length=30)

class Fill_SEBI2(models.Model):
    date=models.CharField(max_length=30)
    equity_gross_pur=models.FloatField(max_length=30)
    equity_gross_sal=models.FloatField(max_length=30)
    equity_net_pur=models.FloatField(max_length=30)
    debt_gross_pur=models.FloatField(max_length=30)
    debt_gross_sal=models.FloatField(max_length=30)
    debt_net_pur=models.FloatField(max_length=30)
