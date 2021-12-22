from django.views.generic import TemplateView
from charts.models import Editor

# Creating views
class EditorChartView(TemplateView):
    template_name = 'charts/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editors"] = Editor.objects.all()
        return context
