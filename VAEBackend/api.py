import os
import json
import base64
import numpy as np
from django.http import *
from PIL import Image
from io import BytesIO
from .utils import *
# from .cluster.cluster import cluster

def vec2img(request):
    return validate_get_request(request, _vec2img)


def _vec2img(request):
    means = request.GET.getlist('means[]')
    covar = request.GET.getlist('covar[]')
    # get result of vae
    imgData = getImgFromVAE(means, covar)
    img = Image.fromarray(imgData, 'L')
    output_buffer = BytesIO()
    img.save(output_buffer, format='png')
    encoded = base64.b64encode(output_buffer.getvalue())
    # read an img
    # fp = open('/home/chenzx/workspace/datasets01/clusterRes/368/0.png', 'rb')
    # encoded = base64.b64encode(fp.read())
    return HttpResponse(encoded, content_type='image/png')


def getImgFromVAE(means, covar):
    return np.random.randint(255, size=(200,200), dtype=np.uint8)

