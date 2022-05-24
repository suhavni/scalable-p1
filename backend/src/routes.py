from datetime import datetime

from flask import Flask, jsonify, request
from flask import current_app as app
from . import db
from sqlalchemy.exc import DataError

from .models import Paste

HEADERS = {"title", "content"}

@app.route('/api/paste', methods=['POST'])
def paste():
    try:
        data = request.json
    except:
        return jsonify({ "error": "Neither 'title' nor 'content' was provided" }), 400
    for header in HEADERS:
        if header not in data: 
            return jsonify({ "error": f"'{header}' was not provided" }), 400
        if not isinstance(data[header], str):
            return jsonify({ "error": "Either 'title' or 'content' was not a String type" }), 400

    paste = Paste(title=data["title"], content=data["content"], created_at=datetime.now())

    try:
        db.session.add(paste)
        db.session.commit()
        return jsonify({ "id": paste.id }), 200 # return the correct id

    except DataError:
        return jsonify({ "error": "Either 'title' or 'content' contains too many characters" }), 400

    except Exception:
        return jsonify({ "error": "Something went wrong." }), 400