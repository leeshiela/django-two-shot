from django.urls import path
from receipts.views import (
    show_receipts,
    create_receipt,
    category_list,
    account_list,
    expense_category,
)

urlpatterns = [
    path("", show_receipts, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("categories/create/", expense_category, name="create_category"),
]
