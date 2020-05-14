from pdf2image import convert_from_path
import os
import random
import tqdm
import logging
import PIL
from multiprocessing import Process

# logging defineable
logging.basicConfig(filename='logs.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
def convert():
	path_pdf = './red_pdf'
	path_img = './red_images'
	if not os.path.exists(path_img):
		os.mkdir(path_img)

	# PIL.Image.MAX_IMAGE_PIXELS = 933120000
	# Image.MAX_IMAGE_PIXELS

	pdfs = os.listdir(path_pdf)
	for idx, pdf in enumerate(tqdm.tqdm(pdfs)):
		try:
			file = os.path.join(path_pdf, pdf)
			name = pdf.split('.')[0]
			# output_filename = os.path.join(path_img, name)
			# #
			# if not os.path.exists(output_filename):
			# 	os.mkdir(output_filename)
			#
			# print("file: ", output_filename)
			PIL.Image.MAX_IMAGE_PIXELS = None
			pages = convert_from_path(file, 500)
			# print("pages: ", pages)
			for idx_page, page in enumerate(pages):
				page.save(path_img+'/{}_{}.jpg'.format(idx, idx_page), 'JPEG')
		except Exception as e:
			logging.error("Logging load data", exc_info=True)
			continue

def re_convert():
	data = 'images_1'
	for file in tqdm.tqdm(os.listdir(data)):
		try:
			path_file = os.path.join(data, file)
			if len(os.listdir(path_file)) == 0:
				pdf = file + '.pdf'
				print(path_file)
				PIL.Image.MAX_IMAGE_PIXELS = None
				pages = convert_from_path('pdf/' + pdf, 300)
				# print("pages: ", pages)
				for idx_page, page in enumerate(pages):
					page.save(path_file+'/{}_{}.jpg'.format(file, idx_page), 'JPEG')
		except Exception as e:
			logging.error("Logging load data", exc_info=True)
			continue

if __name__ == '__main__':
    convert()



