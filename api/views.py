from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from api.models import Links
from api.serializers import LinksSerializer
from utils.random import get_random_id_generator

RandomIdGenerator=  get_random_id_generator()

class PingPongView(APIView):
    def get(self, request):
        return Response({"msg": "pong"}, status=200)


class LinksRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class LinksListCreateView(ListCreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

    def post(self, request, *args, **kwargs):
        # If code is not present, create your own
        request.data['code'] = request.data.get('code', RandomIdGenerator.generate())
        return self.create(request, *args, **kwargs)