from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse, redirect

from app.domain.conversation import ConversationMaker
from app.models import Conversation


@login_required
def customer_service_view(request):
    return render(request, "app/customer_service.html")


@login_required
def chat(request, slug):
    conversation = Conversation.objects.get(slug=slug)
    return render(request, "app/conversation.html", {"conversation": conversation})


@login_required
def conversation_initialize(request):
    if request.user.groups.filter(name="Customer Service").exists():
        return redirect(reverse("customer-service"))
    conversation_obj = ConversationMaker(request.user).initialize_conversation()
    if conversation_obj is None:
        messages.error(
            request, "Sorry. All our agents are busy right now. Please try again later!"
        )
        return redirect(reverse("index"))

    return redirect(reverse("chat", kwargs={"slug": conversation_obj.slug}))


@login_required
def conversation_detail(request, pk):
    conversation = Conversation.objects.get(id=pk)
    return render(
        request,
        "app/conversation_detail.html",
        context={"conversation": conversation},
    )
