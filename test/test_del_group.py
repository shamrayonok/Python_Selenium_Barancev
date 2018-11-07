# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_delete_first_groupe(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    time.sleep(2)
    app.group.delete_first_group()
