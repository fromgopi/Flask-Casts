from flask import request, make_response, jsonify
import json


def response(status, message, status_code):
    """
    Helper method to make an Http response
    :param status: Status
    :param message: Message
    :param status_code: Http status code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


def response_auth(status, message, token, status_code):
    """
    Make a Http response to send the auth token
    :param status: Status
    :param message: Message
    :param token: Authorization Token
    :param status_code: Http status code
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message,
        'auth_token': token.decode("utf-8")
    })), status_code


def make_json_response(token, status, message):
    data = {'status': status, 'message': message}
    if status == 200:
        data['auth_token'] = str(token)

    res = json.dumps(data)
    return res
