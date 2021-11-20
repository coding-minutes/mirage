from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from api.models import Links, Logs
from api.serializers import LinksSerializer
from utils.random import get_random_id_generator

RandomIdGenerator = get_random_id_generator()


class PingPongView(APIView):
    def get(self, request):
        return Response({"msg": "pong"}, status=200)


class LogsMixin:
    def register_log(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.method in ('POST', 'PATCH', 'PUT', 'DELETE'):
            code = request.data.get("code", kwargs.get("pk"))
            user = request.data.get('user', request.data.get('author'))
            description = kwargs.get('description')
            Logs.objects.create(user=user, link=queryset.get(code=code), description=description)


class LinksRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView, LogsMixin):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

    def patch(self, request, *args, **kwargs):
        longUrl = request.data.get('longUrl')
        code = kwargs.get('pk')
        oldUrl = self.queryset.get(code=code).longUrl
        description = f"Updated url from {oldUrl} to {longUrl}"
        obj = self.update(request, partial=True,*args, **kwargs)
        self.register_log(request, description=description, *args, **kwargs)
        return obj

    def delete(self, request, *args, **kwargs):
        description = "Delete"
        obj = self.destroy(request, *args, **kwargs)
        instance = super().get_object(request, description=description)
        self.register_log(request, description=description, *args, **kwargs)
        return obj

class LinksListCreateView(ListCreateAPIView, LogsMixin):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

    def post(self, request, *args, **kwargs):
        # If code is not present, create your own
        request.data["code"] = request.data.get("code", RandomIdGenerator.generate())
        obj = self.create(request, *args, **kwargs)
        self.register_log(request, description=f"Created new link",*args, **kwargs)
        return obj
