import uuid

import pytest
from django.urls import reverse

from voos.models import Voo

dados_artigo = {
    "key": "3221",
    "title": "Parsons to develop prototype ground operations center for DARPA’s Blackjack satellites",
    "url": "https://spacenews.com/parsons-to-develop-prototype-ground/",
    "image_url": "https://spacenews.com/wp-content/uploads/2020/03/DARPA-470x470.png",
    "news_site": "SpaceNews",
    "summary": "The Defense Advanced Research Projects Agency.",
    "published_at": "2021-12-11T20:30:12.000Z",
    "updated_at": "2021-12-11T20:30:12.528Z",
    "featured": "False",
    "launches": [],
    "events": []
}


@pytest.fixture
def artigo(db):
    voo = Voo(
        key=1221,
        title='Parsons to develop prototype ground operations center for DARPA’s Blackjack satellites',
        url='https://spacenews.com/parsons-to-develop-prototype-ground/',
        image_url='https://spacenews.com/wp-content/uploads/2020/03/DARPA-470x470.png',
        news_site='SpaceNews',
        summary='The Defense Advanced Research Projects Agency.',
        published_at='2021-12-11T20:30:12.000Z',
        updated_at='2021-12-11T20:30:12.528Z',
        featured=False,
        launches=[],
        events=[]
    )
    voo.save()
    return voo


@pytest.fixture
def generate_token(client, django_user_model):
    kwargs = {'username': "user1", 'password': "bar"}
    django_user_model.objects.create_user(**kwargs)
    payload = kwargs
    url = reverse('token_obtain_pair')
    resposta = client.post(
        url,
        data=payload,
        format='json',
    )
    return resposta.json()['access']


@pytest.fixture
def resp(client):
    return client.get('https://127.0.0.1:8000')


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        kwargs['password'] = '123456'
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


def test_generate_token(generate_token):
    assert generate_token is not None
