from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stipe Webhooks"""

    def __init__(self, request):
        self.request = request

    def event_handler(self, event):
        """Handle a generic/unknown/unexpected webhook event"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
