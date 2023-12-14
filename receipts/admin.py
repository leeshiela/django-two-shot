from django.contrib import admin
from receipts.models import Account, ExpenseCategory, Receipt


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "id",
    ]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "number",
        "id",
    ]


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "vendor",
        "total",
        "tax",
        "date",
    ]
