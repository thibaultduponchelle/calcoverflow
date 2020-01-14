from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render
#from django.shortcuts import render_to_response
from questions.models import Question
from questions.models import Answer
from questions.models import User
from questions.postform import QuestionForm
from questions.postform import AnswerForm
from django.template.context_processors import csrf
import datetime
import markdown
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template import loader

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:10]
    for p in latest_question_list:
      p.answers = len(Answer.objects.filter(question_id=p.id))
      p.user = User.objects.get(id=p.author_id)
      if len(p.title) > 300 :
        p.title = p.title[:300]
        p.title += " ..."
    template = loader.get_template('questions/index.html')
    context = { 'latest_question_list': latest_question_list, }
    return HttpResponse(template.render(context, request))
    #return render(request, 'questions/index.html', {'latest_question_list': latest_question_list}, content_type='application/xhtml+xml')
    #return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
    #return render_to_response('index.html', context={'latest_question_list': latest_question_list})
    #return HttpResponse("Hello, world. You're at the polls index.")

def unanswered(request):
    ids = Answer.objects.all().values('question_id')
    latest_question_list = Question.objects.exclude(id__in = ids).order_by('-pub_date')[:10]
    for p in latest_question_list:
      p.answers = len(Answer.objects.filter(question_id=p.id))
      p.user = User.objects.get(id=p.author_id)
      if len(p.title) > 300 :
        p.title = p.title[:300]
        p.title += " ..."
    template = loader.get_template('questions/index.html')
    context = { 'latest_question_list': latest_question_list, }
    return HttpResponse(template.render(context, request))





def detail(request, question_id):
    try:
      q = Question.objects.get(pk=question_id)
    except:
      raise Http404
    q.content = markdown.markdown(q.content)
    q.user = User.objects.get(id=q.author_id)
    answers = Answer.objects.filter(question_id=q.id)
    for a in answers:
      a.content = markdown.markdown(a.content)
      a.user = User.objects.get(id=q.author_id)
    form = AnswerForm(auto_id=False)
    template = loader.get_template('questions/detail.html')
    context = {'question': q, 'answers': answers, 'form': form}
    return HttpResponse(template.render(context, request))

def post_answer(request, question_id):
    q = Question.objects.get(pk=question_id)
    u = User.objects.get(pk=1)
    content = request.POST.get('content')
    a = Answer(content=content, author=u, pub_date=timezone.now(), votes=0, question_id=question_id)
    a.save()
    return detail(request, question_id)


@login_required
def ask_question(request):
    form = QuestionForm(auto_id=False)
    template = loader.get_template('questions/ask.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
  

def post_question(request):
    u = User.objects.get(pk=1)
    title = request.POST['title']
    content = request.POST['content']
    q = Question(title=title, content=content, author=u, pub_date=timezone.now(), votes=0)
    q.save()
    return detail(request, q.id)


