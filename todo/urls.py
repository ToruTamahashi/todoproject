from django.urls import path
from .views import TodoList
from .views import TodoDetail
from .views import HelloWorldView
from .views import TodoCreate
from .views import TodoDelete
from .views import TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(),name = 'list'),

    #↓DetailViewクラスの機能でprimary_keyに指定されたデータを取り出して表示する
    #/<int:pk>でurlに入力された数字はidのprimary_keyとしてDjangoが認識する
    path('detail/<int:pk>', TodoDetail.as_view(),name = 'detail'),
    path('hello/', HelloWorldView.as_view()),
    path('create/',TodoCreate.as_view(),name = 'create'),

    #<int:pk>で削除する予定のidを指定
    path('delete/<int:pk>', TodoDelete.as_view(),name = 'delete'),

    #更新予定のidを指定
    path('update/<int:pk>', TodoUpdate.as_view(),name = 'update')
]
