from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register (Customer)
admin.site.register (Deposit)
admin.site.register (Wallet)
admin.site.register (Alert)
admin.site.register (Alert1)
admin.site.register (Alert2)
admin.site.register (Pin)
admin.site.register (Transaction)