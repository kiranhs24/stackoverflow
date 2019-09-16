from rest_framework import status

from rest_framework.response import Response

from rest_framework.views import APIView
import requests

from api.throttles import BurstRateThrottle, SustainedRateThrottle


class GetQuestions(APIView):
    """
    """
    throttle_classes = [BurstRateThrottle, SustainedRateThrottle]

    def get(self, request):

        try:
            url = 'https://api.stackexchange.com/2.2/search/advanced/?site=stackoverflow'

            if 'q' in request.GET:
                q = request.GET.get('q')
                url = url + '&q=' + q

            if 'page' in request.GET:
                page = request.GET.get('page')
                url = url + '&page=' +page

            if 'pagesize' in request.GET:
                pagesize = request.GET.get('pagesize')
                url = url + '&pagesize=' + pagesize

            if 'views' in request.GET:
                views = request.GET.get('views')
                url = url + '&views=' + views

            if 'order' in request.GET:
                order = request.GET.get('order')
                url = url + '&order=' + order

            if 'sort' in request.GET:
                sort = request.GET.get('sort')
                url = url + '&sort=' + sort

            print(url)

            response = requests.get(url)
            data = response.json()

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response("Oops !! Something went wrong", status=status.HTTP_400_BAD_REQUEST)
