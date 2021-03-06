from django.db import models

# Create your models here.
class Order(models.Model):
    gid = models.CharField(max_length=20,primary_key=True)
    gname = models.CharField(max_length=200)
    gpic = models.CharField(max_length=250)
    gdesc = models.CharField(max_length=250)
    price = models.IntegerField()
    totalPrice = models.IntegerField()
    priceType = models.CharField(max_length=20)
    totalTimes = models.IntegerField()
    priceUnit = models.IntegerField()
    typeId = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    showPicNum = models.CharField(max_length=20)
    tag = models.CharField(max_length=120)
    buyable = models.CharField(max_length=20)
    regularBuyMax = models.CharField(max_length=20)
    property = models.CharField(max_length=20)   #modify property to oproperty
    priceBase = models.IntegerField()
    wishSetable = models.CharField(max_length=20)
    buyUnit = models.IntegerField()
    goodsType = models.CharField(max_length=20)
    icon = models.CharField(max_length=200)
    showVideos = models.CharField(max_length=200)
    addAttributes = models.CharField(max_length=20)
    flagList = models.CharField(max_length=20)
    channelId = models.CharField(max_length=20)
    subProperty = models.CharField(max_length=20)

    # owner属性
    cid = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    isFirstLogin = models.CharField(max_length=20)
    coin = models.CharField(max_length=20)
    freeCoin = models.CharField(max_length=20)
    total = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    avatarPrefix = models.CharField(max_length=200)
    ip = models.CharField(max_length=20)
    ipaddress = models.CharField(max_length=100)

    # order属性
    ostatus = models.CharField(max_length=20)
    isLimit = models.CharField(max_length=20)
    totalPeriod = models.CharField(max_length=20)
    period = models.CharField(max_length=20,primary_key=True)
    existingTimes = models.CharField(max_length=20)
    calcTime = models.DateTimeField()
    calcTimestamp = models.CharField(max_length=20)
    duobaoTime = models.DateTimeField()
    duobaoTimestamp = models.CharField(max_length=20)
    luckyCode = models.CharField(max_length=20)
    ownerAllCode = models.CharField(max_length=20)
    ownerCost = models.IntegerField()
