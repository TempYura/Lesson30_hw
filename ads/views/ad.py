from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.viewsets import ModelViewSet

from ads.models.ad import Ad
from ads.permissions import IsOwner, IsStaff
from ads.serializers.ad import AdSerializer, AdDetailSerializer, AdListSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES.get('image', None)
        ad.save()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category_id": ad.category_id,
            "image": ad.image.url if ad.image else None,
        }

        return JsonResponse(response, safe=False)


class AdViewSet(ModelViewSet):
    default_serializer = AdSerializer
    queryset = Ad.objects.order_by('-price')
    serializers = {"retrieve": AdDetailSerializer,
                   "list": AdListSerializer}

    default_permission = [AllowAny]
    permissions = {"retrieve": [IsAuthenticated],
                   "update": [IsAuthenticated, IsOwner | IsStaff],
                   "partial_update": [IsAuthenticated, IsOwner | IsStaff],
                   "destroy": [IsAuthenticated, IsOwner | IsStaff]}

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat')
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get('price_from')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)
