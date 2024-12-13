from django.shortcuts import render, get_object_or_404, redirect
from .models import Tumbler
from .forms import TumblerForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView

# View untuk halaman beranda
def beranda(request):
    return render(request, 'beranda.html')

# View untuk halaman pencarian
def pencarian(request):
    return render(request, 'pencarian.html')

# View untuk halaman kategori
def kategori(request):
    return render(request, 'kategori.html')

# View untuk halaman rekomendasi
def rekomendasi(request):
    return render(request, 'rekomendasi.html')

# View untuk halaman promo
def promo(request):
    return render(request, 'promo.html')

# View untuk halaman keunggulan
def keunggulan(request):
    return render(request, 'keunggulan.html')

def tumbler_list(request):
    tumblers = Tumbler.objects.all()
    return render(request, 'tumbler/tumbler_list.html', {'tumblers': tumblers})

def tumbler_detail(request, pk):
    tumbler = get_object_or_404(Tumbler, pk=pk)
    return render(request, 'tumbler/tumbler_detail.html', {'tumbler': tumbler})

def tumbler_create(request):
    if request.method == 'POST':
        form = TumblerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tumbler_list')
    else:
        form = TumblerForm()
    return render(request, 'tumbler/tumbler_form.html', {'form': form})

def tumbler_edit(request, pk):
    tumbler = get_object_or_404(Tumbler, pk=pk)
    if request.method == 'POST':
        form = TumblerForm(request.POST, request.FILES, instance=tumbler)
        if form.is_valid():
            form.save()
            return redirect('tumbler_list')
    else:
        form = TumblerForm(instance=tumbler)
    return render(request, 'tumbler/tumbler_form.html', {'form': form})

def tumbler_delete(request, pk):
    tumbler = get_object_or_404(Tumbler, pk=pk)
    if request.method == 'POST':
        tumbler.delete()
        return redirect('tumbler_list')
    return render(request, 'tumbler/tumbler_confirm_delete.html', {'tumbler': tumbler})

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nama template login kustom