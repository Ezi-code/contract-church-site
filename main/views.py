from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from .models import Event, Sermon, VideoSermon, Contact, EventRegistration


class HomeView(TemplateView):
    template_name = "main/homepage.html"

    # def get_context_data(self, **kwargs: Any):
    #     ctx = {}
    #     return ctx


class AnnouncementView(TemplateView):
    template_name = ""


class EventView(ListView):
    template_name = "main/events.html"
    model = Event
    context_object_name = "events"
    paginate_by = 10


class SermonView(ListView):
    template_name = "main/sermons.html"
    model = Sermon
    context_object_name = "sermons"
    paginate_by = 10


class VideoSermonView(TemplateView):
    template_name = "main/video_sermons.html"
    model = VideoSermon
    context_object_name = "video_sermons"
    paginate_by = 10


class ContactView(View):
    def get(self, request):
        return render(request, "main/contact.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        new_contact.full_clean()
        new_contact.save()
        # send email
        return render(request, "main/contact.html")


class RegisterEventView(View):
    def get(self, request):
        return render(request, "main/register_event.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        number = request.POST.get("number")
        attendee = request.POST.get("attendee")

        new_contact = EventRegistration(
            name=name, mail_or_tel=email, phone=phone, number=number, attendee=attendee
        )
        new_contact.full_clean()
        new_contact.save()
        # send email
        return render(request, "main/register_event.html")
