from django.contrib import admin
from .models import * 
from .forms import *


#モデルを継承、対象の管理画面での挙動をクラスで定義する。
class TopicModelAdmin(admin.ModelAdmin):
    #一覧表示時に表示させるカラム
    list_display    = ["id","name","comment","post_dt"]
    #並び替え
    ordering        = ["-post_dt"]
    #管理画面で編集できるカラム
    fields          = ["name","comment","post_dt"]
    #フォームのバリデーション(forms.pyで定義したものを継承)
    form            = TopicForm


#管理画面で掲示板のテーブルを操作できる
admin.site.register(Topic,TopicModelAdmin)
