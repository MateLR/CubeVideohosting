from .models import ViewCount


class ViewCountMixin:

    @staticmethod
    def get_client_ip(request):
        """
        Получение IP адреса
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_object(self):
        obj = super().get_object()
        ip_address = ViewCountMixin.get_client_ip(self.request)
        ViewCount.objects.get_or_create(article=obj, ip_address=ip_address)
        return obj
