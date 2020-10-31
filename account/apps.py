from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        import account.signals
        print("HERE WE GO AGAIN LOLOLOLO")
