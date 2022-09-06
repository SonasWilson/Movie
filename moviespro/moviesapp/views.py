from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from moviesapp.addform import AddForm
from moviesapp.forms import MovieForm
from moviesapp.models import Movielist


def demo(request):
    movie=Movielist.objects.all()
    context={
            'movie':movie
             }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movielist.objects.get(id=movie_id)

    return render(request,'detail.html',{'movie':movie})

def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        movie=Movielist(name=name,year=year,desc=desc,image=image)
        movie.save()
        return redirect('/')

    return render(request, "add.html")

def update(request,id):
    movie=Movielist.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movielist.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')





