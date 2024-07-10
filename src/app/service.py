from django.contrib.auth.models import Group
from django.db.models import QuerySet

from app.models import Conversation


def get_available_customer_service_employees() -> QuerySet[int]:
    """Returns the customer service employees that are available for new chats. An employee is available
    when he belongs to the Customer Service group and does not have any open chats (marked in the DB as new)

    Returns:
        available_employees (QuerySet): a qs containing the IDs of the available employees
    """
    customer_service_employees = (
        Group.objects.get(name="Customer Service")
        .user_set.all()
        .values_list("id", flat=True)
    )

    unavailable_customer_service_employees = Conversation.objects.filter(
        new=True
    ).values_list("employee", flat=True)

    return customer_service_employees.difference(unavailable_customer_service_employees)


def create_conversation(customer_id, employee_id, slug):
    conversation = Conversation.objects.create(
        slug=slug,
        employee_id=employee_id,
        customer_id=customer_id,
    )
    conversation.save()

    return conversation
