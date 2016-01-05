import numpy as np
import cv2
import glob     
import string 
import os

def main():
    img_dir = 'images/'
    img_processed_dir = img_dir+'processed/'

    if not os.path.exists(img_processed_dir):
        os.makedirs(img_processed_dir)
    img_paths_list = glob.glob(img_dir+'*.jpg')
    if not img_paths_list:
        print 'did you forget to provide the images???'


    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    percent = 10
    current_img_count = 0
    num_images = len(img_paths_list)


    for img_path in img_paths_list:
        img_path_split = string.split(img_path,'/')
        img = cv2.imread(img_path)
        b,g,r = cv2.split(img)
        b_processed = clahe.apply(b)
        g_processed = clahe.apply(g)
        r_processed = clahe.apply(r)
        img_processed = cv2.merge((b_processed,g_processed,r_processed))
        save_path = img_dir+'processed/p_'+img_path_split[1]
        cv2.imwrite(save_path,img_processed)
        
        if (percent/float(100)) < (current_img_count/float(num_images)):
            print'%d' % (percent) + "%"+' processed'
            percent = percent+10
        current_img_count = current_img_count+1
        
        if percent == 100:
            print '100'+"%"+' processed'

        
if __name__ == '__main__': main()