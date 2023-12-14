from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from receipts.forms import CreateReceipt
from django.contrib.auth.decorators import login_required


@login_required
def show_receipts(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/receipts.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateReceipt(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateReceipt()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_receipt.html", context)
