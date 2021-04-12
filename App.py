# cd /Users/leekwunfung/Documents/GitHub/TrainingDataSynthesis-ImageAddNoise
# python3 App.py
import AddNoise
import cv2

from shutil import copyfile
import random



def duplicate(fn,func,img):
	# hash_ = random.getrandbits(128)
	# ffn = str(hash_)+'_'+func
	ffn = fn+'_'+func
	cv2.imwrite('./data/'+ffn+'.jpg',img)
	copyfile('./data/'+fn+'.txt', './data/'+ffn+'.txt')
	copyfile('./data/'+fn+'.xml', './data/'+ffn+'.xml')

def pro(fn):
	img = cv2.imread('./data/'+fn+'.jpg')
	duplicate(fn,'rain',AddNoise.add_rain(img))
	duplicate(fn,'snowNrain',AddNoise.add_snow( AddNoise.add_rain(img) ) )
	duplicate(fn,'rectangleNrain',AddNoise.rectangle( AddNoise.add_rain(img) ))
	duplicate(fn,'speckleNshadow',AddNoise.speckle( AddNoise.add_shadow(img) ) )
	duplicate(fn,'shadowNrain',AddNoise.add_shadow( AddNoise.add_rain(img) ) )
	duplicate(fn,'speckleNrain',AddNoise.add_rain( AddNoise.speckle(img) ) )
	duplicate(fn,'allNoise',AddNoise.allNoise(img))

pro('11_1_i_h__20190621093202_27871908')