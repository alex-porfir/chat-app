from django.contrib.auth.models import Group

from app.models import Conversation


def get_available_free_customer_service_employees() -> list[int]:
    customer_service_employees = (
        Group.objects.get(name="Customer Service")
        .user_set.all()
        .values_list("id", flat=True)
    )

    unavailable_customer_service_employees = Conversation.objects.filter(
        new=True
    ).values_list("employee", flat=True)

    available_employees = customer_service_employees.difference(
        unavailable_customer_service_employees
    )

    return available_employees


def create_conversation(customer, employee, slug):
    conversation = Conversation.objects.create(
        slug=slug,
        employee=employee,
        customer=customer,
    )
    conversation.save()

    return conversation
