from django.shortcuts import render,redirect
from .forms import Form
from .models import Data
from django.contrib import messages

# Create your views here.

def index_view(request):
    context={}
    if request.method=='POST':

        try:
            with open('testfile.txt', 'w') as file:

                print(file.name)


        except FileNotFoundError:
            print('there was some error in opening in file')

        redirect('index_view')
    try:
        with open('testfile.txt', 'r') as file:
            f_contents=[]
            print(file.name)
            f1=file.readlines()
            for line in f1:
                f_contents.append(line)
            print(f_contents)
            context={
                'f_contents':f_contents,
            }
    except FileNotFoundError:
        print('there was some error in opening in file')

    return render(request,'index.html',context)



def form_view(request):
    title="submit"
    form=Form(request.POST or None)

    if form.is_valid():
        data=form.save(commit=False)
        try:
            with open('testfile.txt','a') as file:

                file.write(str(data.primary_field))
                file.write(',')
                file.write(data.first_field)
                file.write(',')
                file.write(data.second_field)
                file.write(',')
                file.write(data.third_field)
                file.write("\n")

        except FileNotFoundError:
            print('there was some error in opening in file')
        data.save()
        return redirect('index_view')


    context={
        'form':form,
        'title':title
    }

    return render(request,'form.html',context)


def receive_view(request,id=None):

    print('something is going to get wrong lets see that out')

    file=open('testfile.txt', 'a')
    file.write('receive has been visited\n')
    file.close()
    try:
        with open('testfile.txt', 'a') as file:
            file.write(str(id))
            file.write("\n")

    except FileNotFoundError:
        print('there was some error in opening in file')

    return redirect('index_view')