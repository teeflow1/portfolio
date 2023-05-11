from django.shortcuts import render

# Create your views here.
def portfolio_app(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, "contact.html", {})
