from flask import Flask, request, jsonify
from models import Note

app = Flask(__name__)


notes = []


@app.route("/notes/")
def get_notes():
    ser = [note.serialize() for note in notes]
    return jsonify(ser), 200

@app.route("/note/<id>")
def get_note(id):
    note = next((note for note in notes if note.id ==int(id)),None)
    if note:
        return jsonify(note.serialize()), 200
    return "Not Found", 404

@app.route("/note/update/<id>", methods=["PUT"])
def update_note(id):
    note = next((note for note in notes if note.id ==int(id)),None)
    if note:
        data = request.get_json()
        note.txt=data.get("txt")
        return jsonify(note.serialize()), 200
    
    return "Not Found", 404

@app.route("/note/create", methods=["POST"])
def create_note():
    data = request.get_json()
    note = Note(txt=data.get("txt"))
    notes.append(note)
    return jsonify(note.serialize()), 201

@app.route("/note/delete/<id>", methods=["DELETE"])
def delete_note(id):
    note = next((note for note in notes if note.id ==int(id)),None)
    if note:
        notes.remove(note)
        return "OK", 200
    return "Not Found", 404


if __name__ == "__main__":
    app.run()
