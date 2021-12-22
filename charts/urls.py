from django.urls import path

from charts.views import EditorChartView

urlpatterns = [path('', EditorChartView.as_view(), name='index')]
