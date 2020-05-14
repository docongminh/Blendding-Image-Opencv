import cv2
import glob
import tqdm

for path in tqdm.tqdm(glob.glob('output/*.jpg')):
	name = path.split('/')[-1]
	img = cv2.imread(path)
	h, w, _ = img.shape
	cropped = img[420:h-500, 400:w-400]
	cv2.imwrite('cropped/black/{}'.format(name), cropped)