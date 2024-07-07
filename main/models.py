from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='media/announcements/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='media/events/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='media/sermons/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PrayerRequest(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VideoSermon(models.Model):
    preacher = models.CharField(max_length=100)
    video = models.FileField(upload_to='medai/videos/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preacher + "Video Sermon"

class AudioSermon(models.Model):
    preacher = models.CharField(max_length=100)
    audio = models.FileField(upload_to='medai/audios/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preacher + "Audio Sermon"


class NewsLetterSubscription(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " Contact"