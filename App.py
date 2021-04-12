# cd /Users/leekwunfung/Documents/GitHub/TrainingDataSynthesis-ImageAddNoise
# python3 App.py
import AddNoise
import cv2

from shutil import copyfile
import random

fDir = './data/'
tDir = './dataWithNoise/'

def duplicate(fn,func,img):
	# hash_ = random.getrandbits(128)
	# ffn = str(hash_)+'_'+func
	ffn = fn+'_'+func
	cv2.imwrite(tDir+ffn+'.jpg',img)
	copyfile(fDir+fn+'.txt', tDir+ffn+'.txt')
	copyfile(fDir+fn+'.xml', tDir+ffn+'.xml')

def pro(fn):
	print(fn)
	img = cv2.imread(fDir+fn+'.jpg')
	duplicate(fn,'rain',AddNoise.add_rain(img))
	duplicate(fn,'snowNrain',AddNoise.add_snow( AddNoise.add_rain(img) ) )
	duplicate(fn,'rectangleNrain',AddNoise.rectangle( AddNoise.add_rain(img) ))
	duplicate(fn,'speckleNshadow',AddNoise.speckle( AddNoise.add_shadow(img) ) )
	duplicate(fn,'shadowNrain',AddNoise.add_shadow( AddNoise.add_rain(img) ) )
	duplicate(fn,'speckleNrain',AddNoise.add_rain( AddNoise.speckle(img) ) )
	duplicate(fn,'allNoise',AddNoise.allNoise(img))

import os
for file in os.listdir(fDir):
	if '.jpg' in file:
		pro(file.replace('.jpg',''))