from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blog'
    ordering = ['-created_at'] 

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'summary', 'body'] 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title','summary','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')