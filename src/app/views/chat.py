from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse, redirect
from authentication.models import User  # noqa
from app.domain.conversation import ConversationMaker
from app.models import Conversation


@login_required
def customer_service_view(request):
    return render(request, "app/customer_service.html")


@login_required
def chat(request, slug):
    conversation_obj = Conversation.objects.get(slug=slug)
    return render(request, "app/conversation.html", {"conversation": conversation_obj})


@login_required
def conversation_initialize(request):
    conversation_obj = ConversationMaker(request.user).initialize_conversation()
    if conversation_obj is None:
        messages.error(
            request, "Sorry. All our agents are busy right now. Please try again later!"
        )
        return redirect(reverse("index"))

    return redirect(reverse("chat", kwargs={"slug": conversation_obj.slug}))


print("Remove this statement")
