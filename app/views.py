from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import CheckList, CheckListItem
from app.serializers import CheckListItemSerializer, CheckListSerializer
from app.permissions import IsOwner

# Create your views here.

@api_view(['GET',])
def test_api_view(request):
    return Response({'name':'Django test api'})

class TestAPIView(APIView):
    def get(self, request):
        return Response({'name':'Django TEST API CBV '})


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    # IsOwner applies on POST methods not on get methods by using APIView
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get(self, request):
        # queryset = CheckList.objects.all()
        # to get only loggedin user checklist objects
        queryset = CheckList.objects.filter(user=self.request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request':self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_object(self, pk):
        try:
            obj = CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except CheckList.DoesNotExist:
            return Http404

    def get(self, request, pk):
        checklist_object = self.get_object(pk)
        serializer = self.serializer_class(checklist_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        checklist_object = self.get_object(pk)
        serializer = self.serializer_class(checklist_object, data=request.data, context={'request':self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checklist_object = self.get_object(pk)
        checklist_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner, ]

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request':self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListItemAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_object(self, pk):
        try:
            # return CheckListItem.objects.get(pk=pk)
            obj = CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except CheckList.DoesNotExist:
            return Http404

    def get(self, request, pk):
        checklistitem_object = self.get_object(pk)
        serializer = self.serializer_class(checklistitem_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        checklistitem_object = self.get_object(pk)
        serializer = self.serializer_class(checklistitem_object, data=request.data, context={'request':self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checklistitem_object = self.get_object(pk)
        checklistitem_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
