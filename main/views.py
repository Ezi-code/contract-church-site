from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from .models import Event, Sermon,VideoSermon


class HomeView(TemplateView):
    template_name = 'main/homepage.html'
    
    # def get_context_data(self, **kwargs: Any):
    #     ctx = {}
    #     return ctx


class AnnouncementView(TemplateView):
    template_name = ''


class EventView(ListView):
    template_name = 'main/events.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 10

class SermonView(ListView):
    template_name = 'main/sermons.html'
    model = Sermon
    context_object_name = 'sermons'
    paginate_by = 10

class VideoSermonView(TemplateView):
    template_name = 'main/video_sermons.html'
    model = VideoSermon
    context_object_name = 'video_sermons'
    paginate_by = 10


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # send email
        return render(request, 'main/contact.html')