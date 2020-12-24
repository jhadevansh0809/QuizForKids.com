from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import Question
from django.http import Http404

# Create your views here.

def home(request):
    return render(request,'quiz/home.html')


def attempt(request):
    form=Question.objects.all()
    fir=Question.objects.first()
    las=Question.objects.last()
    context={ 'form':form }
    if request.method == 'POST':
        attempt.count=0
        for i in range(fir.id,las.id+1):
            try:
                a=Question.objects.get(id=i)
                lst=list()
                lst.append(a.option1)
                lst.append(a.option2)
                lst.append(a.option3)
                lst.append(a.option4)
                for i,j in enumerate(lst):
                    if j==a.answer:
                        final="option"+str(i+1)
                name=str(a.id)
                selected_option = request.POST[name]
                if selected_option==final:
                    attempt.count=attempt.count+1
            except:
                pass
        return redirect('result')
    return render(request,'quiz/quiz.html',context)


def result(request):
    try:
        res=Question.objects.all()
        length=len(res)
        context={'count':attempt.count,'res':res,'length':length}
        return render(request,'quiz/result.html',context)
    except:
        raise Http404("Kindly attempt the quiz")
