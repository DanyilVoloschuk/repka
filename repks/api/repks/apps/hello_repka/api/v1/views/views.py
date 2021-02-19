from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloRepkaView(APIView):

    def get_text(self):
        return 'hello, repka'

    def get(self, request):
        return Response(self.get_text())
