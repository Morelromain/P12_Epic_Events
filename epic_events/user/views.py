from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import Group

from .models import User
from .serializers import UserSerializer
from .serializers import GroupSerializer
from .perm import UserPermission, GroupPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [(UserPermission & permissions.IsAuthenticated)]

    @action(detail=False, methods=['GET'])
    def my_own_user(self, request, **kwargs):
        queryset = self.get_queryset().filter(username=self.request.user)
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed.
    """

    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [(GroupPermission & permissions.IsAuthenticated)]
