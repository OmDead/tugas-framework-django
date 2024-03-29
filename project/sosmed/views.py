from django.shortcuts import render, redirect

# Create your views here.

from .models import Instagram
from .forms import InstagramForm


def delete(request,delete_id):
	Instagram.objects.filter(id=delete_id).delete()
	return redirect('sosmed:list')

def create(request):
	akun_form = InstagramForm(request.POST or None)
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()
		return redirect('sosmed:list')
	context = {
		"page_title":"sosmed",
		"akun_form":akun_form,
	}
	return render(request,'sosmed/create.html',context)

def list(request):
	semua_akun = Instagram.objects.all()
	context = {
		'page_title':'Sosial Media Penghuni Kos Ade Alip',
		'semua_akun':semua_akun,
	}
	return render(request,'sosmed/list.html',context)