import cv2
import numpy as np
import tqdm
import glob
import os
import time
import logging
from multiprocessing import Process


logging.basicConfig(filename='logs/change_color.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def change_color(images, target_1, target_2, threshold, output='color_changed'):
	"""
		Check color of each pixel
		if mean of all color value of each pixel bigger than threshold:
			color value assign for tartget_1 color
		else:
			color value assign for target_2 color
	"""
	if os.path.exists(output):
		os.makedirs(output)
	counter = []
	paths = glob.glob(images + '/*.jpg')
	for path in tqdm.tqdm(paths):
		start = time.time()
		try:
			img = cv2.imread(path)
			for i in range(img.shape[1]):
			    for j in range(img.shape[0]):
			        channels_xy = img[j,i]
			        if np.mean(channels_xy) > threshold:    
			            img[j,i] = target_1
			        else:
			            img[j,i] = target_2
			saver = os.path.join(output, path.split('/')[-1])
			cv2.imwrite(saver, img)
		except Exception as e:
			logging.error("log exception change color text", exc_info=True)
			continue
		counter.append(time.time() - start)
	print("Total time: {} and average time: {}".format(sum(counter), sum(counter)/len(counter)))


if __name__ == '__main__':

	images = 'test'
	red = [0, 0, 255] # BGR
	white = [255, 255, 255] 
	threshold = 120
	num_thread = 16
	change_color(images, white, red, threshold)
	# processes = []

	# for i in range(num_thread):
	# 	p = Process(target=change_color, args=(images, white, red, threshold))
	# 	p.daemon = True
	# 	p.start()
	# 	processes.append(p)

	# for p in processes:
	# 	p.join()

