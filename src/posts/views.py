from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.


def post_create(request):
	form = PostForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form": form,
	}
	return render(request, "post-form.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Post,id=id)
	context = {
		"instance":instance,
		"title": instance.title,
	}
	return render(request, "post-detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list":queryset,
		"title": "list",
	}
	return render(request, "index.html", context)

def post_update(request, id= None):
	instance = get_object_or_404(Post,id=id)
	
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance":instance,
		"title": instance.title,
		"form": form,
	}
	return render(request, "post-form.html", context)

def post_delete(request):
	return HttpResponse("<h1> Delete</h1>")

