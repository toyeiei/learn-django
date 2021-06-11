from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from core.models import Profile, Email
from core.forms import SubscriberForm
from core.serializers import SubscriberSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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


class SubscriberAPIView(APIView):
    def get(self, request):
        # data = {
        #     "text": "Hello World!",
        # }
        # return JsonResponse(data)

        subscriber = Email.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)