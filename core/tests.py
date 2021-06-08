from django.test import TestCase
from core.models import Profile, Email

class TestProfile(TestCase):
    def test_profile_should_have_fields(self):
        profile = Profile.objects.create(
            name = "toyeiei",
            company = "odds",
        )

        assert profile.name == "toyeiei"
        assert profile.company == "odds"

class TestIndexView(TestCase):
    def test_index_view_should_see_my_name(self):
        # Given
        Profile.objects.create(name = "toyeiei")

        # When
        response = self.client.get("/")

        # Then
        assert response.status_code == 200
        assert "toyeiei" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given
        Profile.objects.create(name = "toyeiei")

        # When
        data = {
            "email": "toy@odds.team"
        }
        response = self.client.post("/", data=data)
        
        # Then
        email = Email.objects.last()
        assert email.email == "toy@odds.team"
