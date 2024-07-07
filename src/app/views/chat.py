import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import reverse, redirect
from django.utils.text import slugify

from app.models import Room


@login_required
def index(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, "app/room.html", {"name": room.name, "slug": room.slug})


@login_required
def room_create(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        uid = str("".join(random.choices(string.ascii_letters + string.digits, k=4)))
        room_slug = slugify(room_name + "_" + uid)
        room = Room.objects.create(name=room_name, slug=room_slug)
        return redirect(reverse("chat", kwargs={"slug": room.slug}))
    else:
        return render(request, "app/create.html")


@login_required
def room_join(request):
    if request.method == "POST":
        room_slug = request.POST["room_slug"]
        room = Room.objects.get(slug=room_slug)
        return redirect(reverse("chat", kwargs={"slug": room.slug}))
    else:
        return render(request, "app/join.html")
