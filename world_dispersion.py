import matplotlib.pyplot as plt;
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv, rgba2rgb
from skimage.viewer import ImageViewer


image_x = imread('bx.png');


img = rgb2hsv(rgba2rgb(image_x))

view = ImageViewer(img)
view.show()