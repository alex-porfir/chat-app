import random  # noqa
import string  # noqa
from authentication.models import User
from app.service import (
    create_conversation,
    get_available_free_customer_service_employees,
)


class ConversationMaker:
    def __init__(self, user: User):
        self.user = user

    def _generate_random_slug(self):
        return str("".join(random.choices(string.ascii_letters + string.digits, k=10)))

    def _get_random_customer_service_employee(self):
        available_employees = get_available_free_customer_service_employees()

        return random.choice(available_employees) if available_employees else None

    def initialize_conversation(self):
        if employee := self._get_random_customer_service_employee():
            employee_obj = User.objects.get(id=employee)
            conversation = create_conversation(
                customer=self.user,
                employee=employee_obj,
                slug=self._generate_random_slug(),
            )

            return conversation
        return None
