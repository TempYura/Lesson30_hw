import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.pk,
            "name": category.name
        })

@method_decorator(csrf_exempt, name='dispatch')
class CatListCreateView(View):
    def get(self, request):
        cat_list = Category.objects.all()
        return JsonResponse([{
            "id": cat.pk,
            "name": cat.name,
        } for cat in cat_list], safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        new_cat = Category.objects.create(**cat_data)
        return JsonResponse({
            "id": new_cat.pk,
            "name": new_cat.name
        })
