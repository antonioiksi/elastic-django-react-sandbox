import base64
import zlib
from rest_framework import views, status
from rest_framework.response import Response


class DecodeIndexView(views.APIView):
    """
    get:
    Decode index name intp human readable
    """
    def get(self):
        user = self.request.user
        indexname = self.kwargs['indexname']
        try:
            decoded = zlib.decompress(base64.b32decode(indexname, True), 40).decode()
            return Response( decoded, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('"errorMessage":%s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)