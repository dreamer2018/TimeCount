#! -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

# 时间点
class TimePoint(models.Model):
    title = models.CharField(max_length=128, null=False)
    describe = models.TextField(max_length=2048, null=False)
    timestamp = models.FloatField(null=False)
    
    @staticmethod
    def get_timestamp_by_id(tid):
        try:
            tp = TimePoint.objects.get(id=tid)
        except TimePoint.DoesNotExist:
            return None
        return tp


class UploadImg(models.Model):
    title = models.CharField(max_length=128, null=False)
    describe = models.CharField(max_length=2048, null=True)
    path = models.CharField(max_length=256)

    @staticmethod
    def get_path_by_id(uid):
        try:
            ul = UploadImg.objects.get(id=uid)
        except UploadImg.DoesNotExist:
            return None
        return ul