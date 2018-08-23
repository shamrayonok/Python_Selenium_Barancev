# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_groupe(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="sdfgbdfg", header="fgbdfgbdfg", footer="dfgbdfgbdfg"))
    app.logout()

def test_add_empty_groupe(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
