from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *

#フォームをインポート
from .forms import *

from django.utils import timezone

#Viewを継承してGET文、POST文の関数を作る
class BbsView(View):

    def reference(self):

        form        = TopicForm()
        topic_data  = Topic.objects.order_by("-post_dt")

        return form,topic_data

    def get(self, request, *args, **kwargs):

        form,topic_data     = self.reference()

        context     = { "data"  : topic_data,
                        "form"  : form }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        #フォームの値を受け取ったらバリデーションする。
        if "name" in request.POST and "comment" in request.POST:

            data    = { "name"      : request.POST["name"],
                        "comment"   : request.POST["comment"],
                        "post_dt"   : timezone.now(),
                        }
            formset = TopicForm(data)
        
            #バリデーションチェック
            if formset.is_valid():
                #DBに記録する
                formset.save()
            else:
                print("バリデーションエラー")

        form,topic_data     = self.reference()

        context     = { "data"  : topic_data,
                        "form"  : form }

        return render(request,"bbs/index.html",context)

index       = BbsView.as_view()


