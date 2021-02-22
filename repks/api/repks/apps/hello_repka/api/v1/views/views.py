from rest_framework.views import APIView
from rest_framework.response import Response


class HelloRepkaView(APIView):

    @staticmethod
    def get_text():
        return 'hello, repka'

    def get(self, request):
        return Response(self.get_text())
