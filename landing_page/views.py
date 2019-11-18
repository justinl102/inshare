from django.shortcuts import render

# Create your views here.
from landing_page.forms import ContactForm
from django.shortcuts import render
# add to your views
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})