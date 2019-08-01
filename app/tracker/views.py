from django.shortcuts import render, redirect

import logging
import random
from datetime import timedelta

from .forms import TrackerForm

logger = logging.getLogger("tracker")


def generate_dummy_data(start_date, end_date):
    price = random.randint(1500, 9000)

    return price


def get_data(request):
    if request.method == "POST":
        form = TrackerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_in = cd["check_in"]
            check_out = cd["check_out"]

            days = (check_out - check_in).days

            for day in range(days):
                start = check_in + timedelta(days=day)
                end = check_in + timedelta(days=day+1)

                price = generate_dummy_data(start, end)

                ota = dict(form.CHOICES)[int(cd["ota"])]

                data = {"URl": "https://{}.com".format(ota.lower()),
                        "Hotel": cd["hotel"],
                        "Search": cd["search"],
                        "Check In": str(start),
                        "Check Out": str(end),
                        "Price": price}
                logger.info("", extra=data)
            return redirect("/")
    else:
        form = TrackerForm()

    return render(request, "tracker.html", {"form": form})
