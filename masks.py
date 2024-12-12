import os
import sys
import cv2
import json
import glob
import shutil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def shapes_dictionary(annotation_path):    
    with open(annotation_path) as handle:
        data = json.load(handle)
    shapes = data['shapes']
    
    return shapes


def binary_mask(image, shapes):    
    blank = np.zeros(shape=(image.shape[0], image.shape[1]), dtype=np.float32)
    for shape in shapes:
        points = np.array(shape['points'], dtype=np.int32)
        cv2.fillPoly(blank, [points], 255)

    return blank


def plot_pair(images, gray=False):
    fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(10,8))
    i=0
    for y in range(2):
        if gray:
            axes[y].imshow(images[i], cmap='gray')
        else:
            axes[y].imshow(images[i])
        axes[y].get_xaxis().set_visible(False)
        axes[y].get_yaxis().set_visible(False)
        i+=1

    return fig


def main():
    images_list = sorted(glob.glob('images/*.jpg'))
    annotations_list = sorted(glob.glob('annotations/*.json'))
    for image_filename, annotation_filename in zip(images_list, annotations_list): 
        filename = image_filename.split('/')[-1].split('.jpg')[0]+'.png'   
        image = cv2.imread(image_filename, 0)
        shapes = shapes_dictionary(annotation_filename)
        mask = binary_mask(image, shapes)
        pair = plot_pair([image, mask], gray=True)
        cv2.imwrite(os.path.join('masks', filename), mask)
        pair.savefig(os.path.join('pairs', filename), bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
	main()
