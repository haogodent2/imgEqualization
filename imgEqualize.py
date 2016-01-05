import numpy as np
import cv2
import glob     

def main():
    

    img_dir = 'images/'
    img_paths_list = glob.glob(img_dir+'*.jpg')
    if not img_paths_list:
        print 'did you forget to provide the images???'

    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    
    for img_path in img_paths_list:
        img = cv2.imread(img_path)
        b,g,r = cv2.split(img)
        b_processed = clahe.apply(b)
        g_processed = clahe.apply(g)
        r_processed = clahe.apply(r)
        img_processed = cv2.merge((b_processed,g_processed,r_processed))
        cv2.imwrite(img_dir+'test.jpg',img_processed)

        print img_path + ' processed'
       
        
if __name__ == '__main__': main()