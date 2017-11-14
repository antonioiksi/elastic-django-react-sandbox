from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes, api_view



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def test_auth_free(request):
    """Пример rest API без авторизации
    """
    #print(request.user)
    return Response([{"message":"Hello world!"}])

#class QuerySerializer(serializers.Serializer):
    #query = serializers.CharField()