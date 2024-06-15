from django.shortcuts import render

# Create your views here.

def home(request):
    personalities = Personalities.objets.all()

    data = {
        'personalities' : personalities,
    }
    return render(request, 'santhalMirror/santhalMirror.html', context = data)
    
def Personalities(request):
    data = {
        'personalities': personalities,
    }
    return render(request,'santhalMirror/santhalMirrorContext.html', context = data)