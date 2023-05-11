from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .models import Score


class HomeView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        try:
            score = Score.objects.get(user=request.user)
        except:
            score = Score.objects.create(user=request.user, high_score=0)
        return render(request, 'home/index.html', {'high_score': score.high_score})

    def post(self, request):
        score = Score.objects.get(user=request.user)
        new_score = int(request.POST['score'])

        if new_score > score.high_score:
            score.high_score = new_score
            score.save()
        return redirect('home:home')

