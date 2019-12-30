from django.shortcuts import render
#ListViewはDjangoで用意されているクラス
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


# Create your views here.
class TodoList(ListView):
    #呼び出すテンプレートのファイル名
    template_name = 'list.html'
    #使用するモデルを指定(list.htmlでそれではTodoModelを使用できるようになる)
    model = TodoModel
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class HelloWorldView(TemplateView):
    template_name = "hello.html"

class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel

    #作成するモデルの項目を選択する属性
    fields = ('title', 'memo', 'priority', 'dudate')
    #success_url:createが成功したときにリダイレクトさせるurlを保存
    #reverse_lazy:リダイレクトするurlを指定するクラス
    #urls.pyでlistという名前に紐づけられたurlにとばす
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    #更新するするモデルの項目を選択する属性
    fields = ('title', 'memo', 'priority', 'dudate')
    success_url = reverse_lazy('list')