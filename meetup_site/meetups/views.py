from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()
    return render(
        request, "meetups/index.html", {"meetups": meetups, "showmeetups": True}
    )


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registrationform = RegistrationForm()
        else:
            registrationform = RegistrationForm(request.POST)
            if registrationform.is_valid():
                user_email = registrationform.cleaned_data["email"]
                participant, created = Participant.objects.get_or_create(
                    email=user_email,
                    defaults={
                        "name": registrationform.cleaned_data["name"],
                        "phone": registrationform.cleaned_data["phone"],
                    },
                )
                selected_meetup.Participants.add(participant)
                return redirect("confirm-registration", meetup_slug=meetup_slug)

        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup_title": selected_meetup.title,
                "meetup_description": selected_meetup.description,
                "meetup": selected_meetup,
                "meetup_found": True,
                "forms": registrationform,
            },
        )
    except Meetup.DoesNotExist:
        return render(
            request,
            "meetups/meetup-detail.html",
            {"meetup_found": False, "forms": registrationform},
        )


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, "meetups/registered.html")


def about(request):
    return render(request, "meetups/about.html")
