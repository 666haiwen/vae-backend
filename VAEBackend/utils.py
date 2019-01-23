import os
import json
import h5py
import sys
import numpy as np
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest


def validate_get_request(request, func, accept_params=None, args=None):
    """Check if method of request is GET and request params is legal

    Args:
         request: request data given by django
         func: function type, get request and return HTTP response
         accept_params: list type, acceptable parameter list

    Returns:
         HTTP response
    """
    if accept_params is None:
        accept_params = []
    if args is None:
        args = []
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    elif set(accept_params).issubset(set(request.GET)):
        return func(request, *args)
    else:
        return HttpResponseBadRequest('parameter lost!')


def read_json_file(filepath):
    try:
        with open(filepath, encoding='utf-8') as fp:
            return json.load(fp)
    except EnvironmentError:
        return { 'error' : 'File not found!' }
