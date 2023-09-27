import random
import string
import os
from ultralytics import YOLO
import time
import itertools
from glob import glob
from PIL import Image
import argparse
import cv2
import shutil
import numpy as np

images_path = "data/test/images/"
return_letter = ""
images_path_runs = "runs/detect/predict"

def parser():
    parser = argparse.ArgumentParser(description="YOLO American Sign Language Detection")
    parser.add_argument("--letter", type=str, default="",
                        help="image source. It can be a single image, a"
                        "txt with paths to them, or a folder. Image valid"
                        " formats are jpg, jpeg or png."
                        "If no input is given, ")
    parser.add_argument("--thresh", type=float, default=.25,
                        help="remove detections with lower confidence")
    return parser.parse_args()
    

def check_arguments_errors(args):
    assert 0 < args.thresh < 1, "Threshold should be a float between zero and one (non-inclusive)"
    if args.letter.isalpha() == False:
        raise(ValueError("Invalid input letter {}".format(args.letter)))


def load_images(start_letter):
    global return_letter 
    cv2.destroyAllWindows()
    
    images = os.listdir(images_path)
    groups = itertools.groupby(images, lambda t:t[0])
    for key,l in groups:
        for file_name in l:
            if file_name.endswith(".jpg") and file_name.startswith(start_letter):
                return_letter = file_name
    return glob(os.path.join(images_path, return_letter))



def main():
        
        shutil.rmtree(images_path_runs)
        args = parser()
        check_arguments_errors(args)
        
        letter = args.letter
        letter_index = string.ascii_uppercase.index(letter) + 1
        image_letter = load_images(letter)

        if image_letter is not None:
            model = YOLO("best.pt")
            im1 = Image.open(image_letter[0])
            results = model.predict(source=im1, save=True, classes=[letter_index-1])
            result = results[0]
            output = []
            
            for box in result.boxes:
                x1, y1, x2, y2 = [
                    round(x) for x in box.xyxy[0].tolist()
                ]
                class_id = box.cls[0].item()
                prob = round(box.conf[0].item(), 2)
                output.append([
                    x1, y1, x2, y2, result.names[class_id], prob
                ])
                print("Detected Letter : ", result.names[class_id], " with prob : ", prob)
        
        img1 = cv2.imread(os.path.join(images_path, return_letter), cv2.IMREAD_ANYCOLOR)
        img2 = cv2.imread(os.path.join(images_path_runs, return_letter), cv2.IMREAD_ANYCOLOR)
        Horizontal = np.concatenate((img1, img2), axis=1)
        cv2.imshow('American Sign Language', Horizontal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        




if __name__ == "__main__":
    main()

