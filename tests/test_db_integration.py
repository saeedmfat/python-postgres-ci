import os
import pytest
from app.db import get_users

def test_get_users():

    users = get_users()

    assert isinstance(users, list)
    assert len(users) == 2 

    user_names = [user['name'] for user in users]
    assert 'Alice' in user_names
    assert 'Bob' in user_names