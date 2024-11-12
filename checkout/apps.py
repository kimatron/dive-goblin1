from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    AppConfig class for the checkout app
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals  # noqa: F401
