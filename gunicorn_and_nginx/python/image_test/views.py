from django.shortcuts import get_object_or_404, render
from image_test.models import Image

def test_image(request , id):
    image = get_object_or_404(Image, pk=id)
    return render(request , "index.html" ,context= {'image':image})