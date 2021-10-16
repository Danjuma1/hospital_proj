from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogpost
from .forms import PostForm
from django.views.generic import ListView 
from django.utils import timezone


def add_blog_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			
			return redirect('blog_details', post.slug)
	else:
		form = PostForm()
	context = {'form': form}
	return render(request, 'blog/add_blog_post.html', context)

class PostList(ListView):
	model = Blogpost
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(created_date=timezone.now() ).order_by('-created_date')


def post_draft(request):
	draft = Blogpost.objects.filter(status=0).filter(author = request.user).order_by('created_date')
	context = {'draft':draft}
	return render(request, 'blog/post_draft.html', context)

def blog_details(request, post_slug):
	post =  get_object_or_404(Blogpost, slug = post_slug)
	context = {'post': post}
	return render(request, 'blog/blog_details.html', context)
