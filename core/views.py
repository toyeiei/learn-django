from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core.models import Profile, Email
from core.forms import SubscriberForm


# Create your views here.
def index(request):
    html = """
        <h1>Hello, I am Toy Night Owls</h1>
        <h2>I am learning Django</h2>

        <h3>My favorite food</h3>
        <ol>
            <li>Hamburger</li>
            <li>Hotdog</li>
            <li>Ham</li>
        </ol>
    """
    return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        name = "Kasidis Satangmongkol"
        my_team = "Night Owls"
        profile = Profile.objects.get(id=1)

        form = SubscriberForm()

        return render(
            request,
            "index.html",
            {
                "name": name,
                "form": form,
                "food1": "Big Hamburger",
                "food2": "Hotdog",
                "food3": "Ham",
                "my_team": my_team,
                "profile": profile.name,
            },
        )

    def post(self, request):
        print(request.POST)

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_email = form.cleaned_data.get("email")
            Email.objects.create(email=user_email)
            print("Email has been submited to our database.")

        return render(request, "thank-you.html")
