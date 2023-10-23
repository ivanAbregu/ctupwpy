from flask import Flask, jsonify, request
from db import DB


app = Flask(__name__)


@app.route("/api/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST": 
        if "content" in request.json:
            DB.create_note(request.json["content"])
            return "", 201

        return "", 422

    return jsonify([dict(x) for x in DB.select_all_notes()])


@app.route("/api/notes/<note_id>", methods=["GET", "DELETE"])
def note(note_id):
    if request.method == "DELETE":
        if DB.delete_note(note_id):
            return "", 200

        return "", 404
    elif result := DB.select_one_note(note_id):
        return dict(result)

    return "", 404


app.run()