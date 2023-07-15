from django.shortcuts import render
from rest_framework.response import Response
from py_file.cifar10_ui import *
from py_file.input import *

# Create your views here.
path = openfile()
Response(dl_model_image(path))
