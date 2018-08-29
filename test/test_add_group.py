# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sdfgbdfg", header="fgbdfgbdfg", footer="dfgbdfgbdfg"))
    app.session.logout()


def test_add_empty_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
