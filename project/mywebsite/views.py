from django.shortcuts import render

def index(request):
	context = {
		'judul':'Kos Ade Alip',
		'subjudul':'selamat datang',
		'banner':'img/banner_kos.jpeg',
		'app_css':'css/styles.css',

	}
	return render(request,'index.html',context)