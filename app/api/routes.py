from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Image, image_schema, images_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/images', methods = ['POST'])
@token_required
def add_image(current_user_token):
    file_name = request.json['file_name']
    mimetype = request.json['mimetype']
    title = request.json['title']
    upper_cap = request.json['upper_cap']
    lower_cap = request.json['lower_cap']
    user_token = current_user_token.token

    image = Image(file_name, title, user_token, mimetype=mimetype,  upper_cap=upper_cap, lower_cap=lower_cap)

    db.session.add(image)
    db.session.commit()

    response = image_schema.dump(image)
    return jsonify(response)


@api.route('/images', methods = ['GET'])
@token_required
def get_all_images(current_user_token):
    a_user = current_user_token.token
    images = Image.query.filter_by(user_token = a_user).all()

    response = images_schema.dump(images)
    return jsonify(response)


@api.route('/images/<id>', methods = ['GET'])
@token_required
def get_single_image(current_user_token, id):
    image = Image.query.get(id)

    response = image_schema.dump(image)
    return jsonify(response)

@api.route('/images/<id>', methods = ['POST', 'PUT'])
@token_required
def update_image_info(current_user_token, id):
    image = Image.query.get(id)
    image.file_name = request.json['file_name']
    image.mimetype = request.json['mimetype']
    image.title = request.json['title']
    image.upper_cap = request.json['upper_cap']
    image.lower_cap = request.json['lower_cap']
    image.user_token = current_user_token.token

    db.session.commit()

    response = image_schema.dump(image)
    return jsonify(response)


@api.route('/images/<id>', methods = ['DELETE'])
@token_required
def delete_image(current_user_token, id):
    image = Image.query.get(id)

    db.session.delete(image)
    db.session.commit()

    response = image_schema.dump(image)
    return jsonify(response)