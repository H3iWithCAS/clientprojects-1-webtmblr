from django.shortcuts import render, get_object_or_404, redirect
from .models import Tumbler
from .forms import TumblerForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Promo  

# View untuk halaman beranda
def beranda(request):
    query = request.GET.get('q', '')  # Mengambil parameter pencarian dari URL
    if query:
        tumblers = Tumbler.objects.filter(name__icontains=query)  # Filter tumbler berdasarkan nama
    else:
        tumblers = Tumbler.objects.all()  # Jika tidak ada pencarian, tampilkan semua tumbler
    
    return render(request, 'beranda.html', {'tumbler': tumblers, 'query': query})

# View untuk halaman pencarian
def pencarian(request):
    query = request.GET.get('q', '')  # Ambil query dari URL
    if query:
        products = Tumbler.objects.filter(name__icontains=query)  # Filter berdasarkan nama produk
    else:
        products = Tumbler.objects.all()  # Jika tidak ada pencarian, tampilkan semua produk
    
    return render(request, 'pencarian.html', {'products': products, 'query': query})

# View untuk halaman kategori
def kategori(request):
    return render(request, 'kategori.html')

# View untuk halaman rekomendasi
def rekomendasi(request):
    # Ambil produk yang sudah disesuaikan dengan kriteria rekomendasi
    recommended_products = Tumbler.objects.filter(is_recommended=True)  # Contoh filter produk yang direkomendasikan
    return render(request, 'rekomendasi.html', {'recommended_products': recommended_products})

def product_detail(request, id):
    product = get_object_or_404(Tumbler, id=id)  # Ambil objek produk berdasarkan ID
    return render(request, 'product_detail.html', {'product': product})

def recommended_products(request):
    recommended_products = Tumbler.objects.all()  # Ambil semua produk sebagai contoh
    return render(request, 'recommended_products.html', {'recommended_products': recommended_products})

# View untuk halaman promo
def promo(request):
    promos = Tumbler.objects.filter(is_promo=True)  # Filter untuk produk yang memiliki promo
    return render(request, 'promo.html', {'promos': promos})

def promo_detail(request, id):
    promo = get_object_or_404(Promo, id=id)  # Ambil promo berdasarkan ID
    return render(request, 'promo_detail.html', {'promo': promo})

def promo_list(request):
    promos = Promo.objects.all()  # Ambil semua promo dari database
    return render(request, 'promo_list.html', {'promos': promos})

# View untuk halaman keunggulan
def keunggulan(request):
    return render(request, 'keunggulan.html')

# View untuk halaman tumbler
def tumbler_list(request):
    tumblers = Tumbler.objects.all()
    return render(request, 'tumbler_list.html', {'tumblers': tumblers})

def tumbler_detail(request, pk):
    tumbler = get_object_or_404(Tumbler, pk=pk)
    return render(request, 'tumbler_detail.html', {'tumbler': tumbler})

# View untuk halaman login
class CustomLoginView(LoginView):
    template_name = 'login.html'