from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import EventAbstract
from accounts.models import User


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events

class Item(models.Model):
    item = models.CharField(max_length=50, unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.item



class Event(EventAbstract):
    """ Event model """

    ACTIVE_CHOICES = [
        ('비료', '비료'),
        ('농약', '농약'),
        ('인력', '인력')
    ]
    LEVEL_CHOICES = [('경운정지', '경운정지'), ('김매기', '김매기'), ('묘판관리', '묘판관리'),
                     ('물주기', '물주기'), ('병해충방제', '병해충방제'), ('비닐피복및흙덮기', '비닐피복및흙덮기'),
                     ('비닐피복및흙덮기제거', '비닐피복및흙덮기제거'), ('선별및포장', '선별및포장'), ('솎아내기', '솎아내기'), ('수정', '수정'), ('수확', '수확'),
                     ('순지르기및눈따기', '순지르기및눈따기'),
                     ('아주심기', '아주심기'), ('온도관리', '온도관리'), ('운반및저장', '운반및저장'), ('웃비료주기', '웃비료주기'), ('유인', '유인'),
                     ('접목', '접목'),
                     ('제초', '제초'), ('종자준비및소독', '종자준비및소독'), ('지주(네트)세우기', '지주(네트)세우기'), ('탈곡', '탈곡'),
                     ('퇴비및밑비료주기', '퇴비및밑비료주기'), ('파종', '파종'),
                     ('하우스관리', '하우스관리'), ('한때심기', '한때심기'), ('구입및판매', '구입및판매'), ('영농교육', '영농교육'), ('건조', '건조'),
                     ('묘상준비및설치', '묘상준비및설치'), ('비닐씌우기/벗기기', '비닐씌우기/벗기기')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=50, null=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    active = models.CharField(max_length=100, choices=ACTIVE_CHOICES)
    # weather =
    image = models.ImageField(upload_to='images', blank=True, null=True)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)

    objects = EventManager()

    def __str__(self):
        return f"{self.title} - {self.item}"

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=[self.id])

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=[self.id])
        return f'<a href="{url}"> {self.item} </a>'