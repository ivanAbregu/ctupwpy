from main import app
from models import Note
import json
from unittest.mock import patch

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
def test_get_notes():
    note = Note("lorem ipsum")
    with patch('main.notes', [note]):
        response = app.test_client().get('/notes/')
        data = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert len(data) == 1

def test_get_note():
    note = Note("lorem ipsum")
    with patch('main.notes', [note]):
        response = app.test_client().get(f'/note/{note.id}')
        data = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert data.get("id") == note.id


def test_update_note():
    note = Note("lorem ipsum")
    new_txt = {"txt": "qwerty 12345"}
    with patch('main.notes', [note]):
        response = app.test_client().put(f'/note/update/{note.id}', data=json.dumps(new_txt), headers=HEADERS)
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["txt"] == new_txt["txt"]

def test_create_note():
    data = {"txt":"lorem"}
    response = app.test_client().post(f'/note/create', data=json.dumps(data), headers=HEADERS)
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 201
    assert res.get("txt") == data["txt"]

def test_delete_note():
    note = Note("lorem ipsum")
    with patch('main.notes', [note]):
        response = app.test_client().delete(f'/note/delete/{note.id}')
        assert response.status_code == 200