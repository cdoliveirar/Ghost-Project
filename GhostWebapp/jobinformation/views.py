from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Topic, Note


# Create your views here.
#def index_jobinformation(request):
#    return render_to_response("jobinformation/informationtype_list.html","", context_instance=RequestContext(request))

#Item
class TopicList(ListView):
    model = Topic
    fields = ['topic_name']
    template_name =  'jobinformation/topic_list.html'


class TopicNew(CreateView):
    model = Topic
    fields = ['topic_name']
    success_url = reverse_lazy('jobinformation:TopicList')


class TopicUpdate(UpdateView):
    model = Topic
    fields = ['topic_name']
    success_url = reverse_lazy('jobinformation:TopicList')
  
  
class TopicDelete(DeleteView):
    model = Topic
    success_url = reverse_lazy('jobinformation:TopicList')
    
    
# Note
class NoteList(ListView):
    model = Note
    fields = ['text','pup_date']
    template_name = 'jobinformation/note_list.html' 
    
    
class NoteNew(CreateView):
    model = Note
    fields = ['topic','text','pup_date']
    success_url = reverse_lazy('jobinformation:NoteList')
    

class NoteUpdate(UpdateView):
    model = Note
    #fields = ['infotype','info_text','pup_date']
    fields = ['topic','text','pup_date']
    success_url = reverse_lazy('jobinformation:NoteList')
    

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('jobinformation:NoteList')