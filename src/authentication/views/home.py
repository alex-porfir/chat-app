from django.views.generic.base import RedirectView


class HomePageView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Customer Service").exists():
                return "customer_service/"
            return "connect/"
        return "accounts/login/"
