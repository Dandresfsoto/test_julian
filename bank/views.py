from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from .models import Client, Account
from .serializers import ClientSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.response import Response


class ClientAPI(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientIntance(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TransactionAccounAPI(generics.GenericAPIView):

    queryset = Account.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        message = "done"
        status_code = status.HTTP_200_OK
        try:
            instance.new_transaction(
                transaction_type=serializer.validated_data.get("transaction_type"),
                amount=serializer.validated_data.get("amount")
            )
        except ValueError:
            message = "insufficient funds"
            status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": message, "account_amount": str(instance.amount)}, status=status_code)

