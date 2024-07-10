import random
import string
from authentication.models import User
from app.service import (
    create_conversation,
    get_available_customer_service_employees,
)
from app.models import Conversation


class ConversationMaker:
    def __init__(self, user: User):
        self.user = user

    def _generate_random_slug(self) -> str:
        return str(
            "".join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=40,
                )
            )
        )

    def _get_random_customer_service_employee(self) -> User | None:
        available_employees = get_available_customer_service_employees()

        return random.choice(available_employees) if available_employees else None

    def initialize_conversation(self) -> Conversation | None:
        if employee_id := self._get_random_customer_service_employee():
            conversation = create_conversation(
                customer_id=self.user.id,
                employee_id=employee_id,
                slug=self._generate_random_slug(),
            )

            return conversation
        return None
