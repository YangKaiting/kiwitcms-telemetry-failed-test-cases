from django.urls import reverse_lazy


# Follows the format of ``tcms.settings.common.MENU_ITEMS``
MENU_ITEMS = [
    ('Failed Testcases Report', reverse_lazy('telemetry-testruns-get')),
]