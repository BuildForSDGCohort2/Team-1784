from django.apps import AppConfig


class UsersdashboardConfig(AppConfig):
    name = 'usersDashboard'

    def ready(self):
        import usersDashboard.signals
