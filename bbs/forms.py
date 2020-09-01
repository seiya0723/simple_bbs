#モデルのフィールド定義を継承し、フォームとする。
from .models import *
from django.forms import ModelForm,TextInput,Textarea


#ModelFormを継承し、Metaクラスに利用するモデルクラス名、フィールド、ウィジェット等を記述
class TopicForm(ModelForm):
    class Meta:
        model   = Topic
        widgets = { "name": TextInput(attrs={"class":"form-control","placeholder":"名前","autofocus":"",} ),
                    "comment":Textarea(attrs={"class":"form-control","placeholder":"ここにコメントを入力する","rows":"6"} ),
                    }
        fields  = [ "name","comment","post_dt" ]
