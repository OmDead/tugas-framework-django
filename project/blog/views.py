from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'Blog',
		'subjudul':'ini adalah blog Kos Ade Alip',
		'banner':'blog/img/banner_blog.png',
	}
	return render(request,'index.html',context)