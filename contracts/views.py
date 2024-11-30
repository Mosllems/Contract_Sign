from idlelib.debugobj_r import remote_object_tree_item
from urllib.request import Request

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Contract


class HomeView(generic.TemplateView):
    template_name = "home.html"


@login_required
def create_contract(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        email = request.POST["email"]
        contract = Contract.objects.create(
            title=title,
            description=description,
            signer_1=request.user,
            signer_2=email,
        )
        return redirect("sign_contract", contract_id=contract.id)
    return render(request, "contracts/create_contract.html" )


def sign_contract(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == "POST":
        contract.full_name_signer_1 = request.POST["full_name"]
        contract.Is_signed_by_1 = True
        contract.save()
        send_invitation_email(contract.signer_2, contract.id)
        return redirect("success")
    return render(request, "contracts/sign_contract.html", {"contract": contract})


def success(request):
    message = {"Message": "The contract has been signed successfully."}
    return render(request, "contracts/success.html", {"success": message['Message']})


def send_invitation_email(email, contract_id):
    subject = 'Sign the Contract'
    message = f'Please sign the contract here: http://localhost:8000/sign/{contract_id}/second/'
    from_email = 'moslemamiri82@gmail.com'
    send_mail(subject, message, from_email, [email])


def sign_contract_second(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == "POST":
        contract.full_name_signer_2 = request.POST["full_name"]
        contract.Is_signed_by_2 = True
        contract.save()
        return redirect("success_second")
    return render(request, "contracts/sign_contract_second.html", {"contract": contract})


def success_second(request):
    message = {"Message": "The contract has been signed successfully."}
    return render(request, "contracts/success_second.html", {"success": message['Message']})

