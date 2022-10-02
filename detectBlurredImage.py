
import skimage
import numpy as np
from matplotlib import pyplot as plt
# import skimage as sk 
from skimage.color import *
from skimage import io
from skimage import data
from skimage import filters
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature
from skimage import metrics
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.util import img_as_uint


def convu(img , ker):
  img = rgb2gray(img)
  row, col = img.shape[0],img.shape[1]
  krow,kcol = ker.shape[0],ker.shape[1]
  kcx , kcy = kcol/2 , krow/2
  newimg = np.zeros((row,col))

  for i in range(0,row):
    for j in range(0,col):
      for m in range (0,krow):
        mm = (int)(krow - 1 - m)
        for n in range(0,kcol):
          nn = (int)(kcol-1-n)
          ii =(int)( i + kcy - mm)
          jj = (int)(j + kcx - nn)
          if(((ii>=0 and ii<row) and( jj>=0 and jj<col))):
            newimg[i][j] = newimg[i][j] + (img[ii,jj]* ker[mm][nn])
  
  newimg = skimage.exposure.rescale_intensity(newimg, in_range=(0, 255))
  ret = img_as_uint(newimg)
  
  return ret


def Laplacianfilter():
  L = np.array([[0,1,0],[1,-4,1],[0,1,0]])
  return L


def BlurOrNot( imageAddress):
  img = io.imread(imageAddress)
  io.imshow(img)
  img2 = convu(img,Laplacianfilter())

  if(np.var(img2)<100):
    print("Blur\nprobability = ",end = '')
    print((100 - np.var(img2) ),end = ' ')
    print("%")
  else:
    print("not blurred")


BlurOrNot("images/blur2.png")
