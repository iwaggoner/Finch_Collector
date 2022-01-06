# Owner View_Page
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import OwnerSerializer
from ..models.owner import Owner

class OwnerView(APIView):
    def get(self, request):
        print(request.session)
        owners = Owner.objects.all()[:10]
        data = OwnerSerializer(owners, many=True).data
        return Response(data)

    serializer_class = OwnerSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        owner = OwnerSerializer(data=request.data)
        if owner.is_valid():
            b = owner.save()
            return Response(owner.data, status=status.HTTP_201_CREATED)
        else:
            return Response(owner.errors, status=status.HTTP_201_CREATED)
