from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from student_groups.models import Student
from django.http import HttpResponse


# Create your views here.


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):

        group = self.request.user.student.group

        try:
            students = Student.objects.filter(group=group)
        except Student.DoesNotExist:
            students = None

        queryset = []
        for student in students:
            if student.user is not None:
                queryset.append(student.user)
        return queryset

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.IsAuthenticated(),
        return permissions.AllowAny(),


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return User.objects.all()
        uid = self.request.user.id
        return User.objects.all().filter(id=uid)

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
