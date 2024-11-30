from django.contrib import admin
from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = ["title", "signer_1", "signer_2"]


admin.site.register(Contract, ContractAdmin)


