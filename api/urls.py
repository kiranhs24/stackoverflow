from django.conf.urls import url

from api.views import GetQuestions

urlpatterns = [
    url(r'^questions/$', GetQuestions.as_view())
]
