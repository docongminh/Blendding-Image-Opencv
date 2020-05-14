import cv2 as cv
import numpy as np
import glob
import os
import logging
from multiprocessing import Process

if not os.path.exists('logs'):
	os.mkdir('logs')

logging.basicConfig(filename='logs/blending.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


def blending(images: str, background: str, alphas: list):
	"""

	"""
	image_paths = glob.glob(images + '/*.jpg')
	background_paths = glob.glob(background + '/*.jpg')
	for background_path in background_paths:
		for idx, image_path in enumerate(image_paths):
			# try:
			# imread image
			print(image_path)
			img = cv.imread(image_path)
			# x, y, _ = img.shape
			# img_cropped = img[10: y-10, 10: x+10]
			# cv.imwrite('test.jpg', img_cropped)
			# get shape to resize background
			shape = img.shape[1], img.shape[0]
			# imread and resize backround
			backround_name = background_path.split('/')[-1]
			bgr_name = backround_name.split('.')[0]
			img_bgr = cv.imread(background_path)
			bgr_resized = cv.resize(img_bgr, shape)
			# setup save path
			image_name = image_path.split('/')[-1]
			print(image_name)
			name = image_name.split('.')[0]
			print(name)
			saver = 'output_red'
			if not os.path.exists(saver):
				os.makedirs(saver)
			# add blending with alpha
			for alpha in np.asarray(alphas):
			    dst = cv.addWeighted(img, alpha, bgr_resized, 1-alpha, 0)
			    img_path = saver + '/{}_{}_{}_{}.jpg'.format(bgr_name, name, idx, alpha)
			    cv.imwrite(img_path, dst)
			# except Exception as e:
			# 	logging.error("log blending image", exc_info=True)
			# 	continue

if __name__ == '__main__':
	
	images = 'red_images'
	background = 'background'
	alpha = [ 0.5, 0.8]
	processes = []
	for i in range(14):
		p = Process(target=blending, args=(images, background, alpha))
		p.daemon = True
		p.start()
		processes.append(p)

	for p in processes:
		p.join()