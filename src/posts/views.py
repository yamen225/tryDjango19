from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.


def post_create(request):
	form = PostForm(request.POST, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully created")
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
	queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 4) # Show 25 contacts per page
	page = request.GET.get("page")
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list":queryset,
		"title": "list",
	}
	return render(request, "post-list.html", context)

def post_update(request, id= None):
	instance = get_object_or_404(Post,id=id)
	
	form = PostForm(request.POST or None, request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()		
		messages.success(request, "Successfully saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance":instance,
		"title": instance.title,
		"form": form,
	}
	return render(request, "post-form.html", context)

def post_delete(request, id=id):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("post:list")

