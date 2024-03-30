from http import HTTPStatus

from django.http import HttpResponse
from django.test import Client
from django.urls import reverse
from pytest import mark


@mark.django_db
def test_goal_list(client: Client) -> None:
    url: str = reverse('goal-list')
    response: HttpResponse = client.get(url)

    assert response.status_code == HTTPStatus.OK
