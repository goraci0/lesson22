from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm, ArticleForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views (представление) here.

def main_page(request):
    art_all = Article.objects.all()
    return render(request, 'articles/category.html', {'articles':art_all})


def article_description(request,id):
    art_one = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(comment_artc=art_one)
#    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            print(f'{name}, {message}')
            article_object = Comment(comment_autor=name, comment_text=message, comment_artc=art_one)
            article_object.save()
            return render(request, 'articles/single.html', {'article': art_one, 'comments': comments, 'form': form})
    else:
        form = CommentForm()
        return render(request, 'articles/single.html', {'article': art_one, 'comments': comments, 'form': form})

def article_add(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'articles/article_add.html', {'form': form})
    else:
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('articles:index'))
        else:
            return render(request, 'articles/article_add.html', {'form': form})

class CommentListView(ListView):
    model = Comment
    template_name = 'articles/comment_list.html'
    context_object_name = 'comments'

    #def get_queryset(self,id):
    # можно наложить условия на объекты
        #return Comment.objects.filter(comment_artc=id)

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'articles/comment_one.html'


class CommentUpdateView(UpdateView):
    template_name = 'articles/comment_update.html'
    model = Comment
    success_url = reverse_lazy('articles:comment_list')

class CommentDeleteView(DeleteView):
    template_name = 'articles/comment_delete.html'
    model = Comment
    success_url = reverse_lazy('articles:comment_list')

class CommentCreateView(CreateView):
    template_name = 'articles/comment_create.html'
    model = Comment
    fields = '__all__'
    success_url = reverse_lazy('articles:comment_list')