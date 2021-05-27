import cv2 
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def edge_detection(image): 
    edges_detected = cv2.Canny(image , 100, 200)  # Change these values, instead of 100, try writing 70,50 etc, instead of 200, try 150, 125 and see the change in intensity of image
    images = [image , edges_detected]
    location = [121, 122] 
    for loc, edge_image in zip(location, images): 
        plt.subplot(loc) 
        plt.imshow(edge_image, cmap='gray')
        plt.show()

        
# convert image 2.jpeg with imread function and store it in img

# call edge_detection function


