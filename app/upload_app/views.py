from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, generics
from .models import UploadedFile
from .serializers import FileUploadSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser, FormParser]  # Handle file uploads

    def get(self, request, *args, **kwargs):
       # """Retrieve all uploaded files."""
        files = self.get_queryset()
        serializer = self.get_serializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
