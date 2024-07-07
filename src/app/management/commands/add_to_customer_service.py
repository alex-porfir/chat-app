from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group  # noqa
from authentication.models import User  # noqa


class Command(BaseCommand):
    help = (
        "Adds specified users to the customer service group. Leave empty for all users."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "usernames",
            nargs="*",
            type=str,
            help="List of users (identified by username)",
        )

    def handle(self, *args, **options):
        usernames: list[str] = options["usernames"]
        try:
            group = Group.objects.get(name="Customer Service")

            users = (
                User.objects.filter(username__in=usernames)
                if usernames
                else User.objects.all()
            )
            group.user_set.add(*users)

            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully added "%s" to Customer Service group'
                    % [user.username for user in users]
                )
            )
        except Exception:
            raise CommandError("Something unexpected happened!")
