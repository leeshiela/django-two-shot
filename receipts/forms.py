from django import forms
from receipts.models import Receipt, ExpenseCategory


class CreateReceipt(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class CreateCategory(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]
