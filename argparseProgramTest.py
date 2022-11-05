import argparse
 
# Construct the argument parser and parse the arguments
arg_desc = '''\
        Let's load an image from the command line!
        --------------------------------
            This program loads an image
            with OpenCV and Python argparse!
        '''
parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter,
                                    description= arg_desc)
 
parser.add_argument("-i", "--image", metavar="IMAGE", help = "Path to your input image")
parser.add_argument("-f", "--flip", metavar="IMAGE_FLIP", help = "Path to your input image")
args = vars(parser.parse_args())
 
 
if args["flip"]:
    # Flip the image vertically
    print("[INFO] flipping image vertically...")
    flipped = cv2.imread(args["flip"])
    flip_img = cv2.flip(flipped, 0)
    
    # Display the flipped image and press any key to stop
    cv2.imshow("Flipped vertically", flip_img)
    
else:
    # Load the image with "cv2.imread"
    image = cv2.imread(args["image"])
    # Display the original image
    cv2.imshow("Image", image)
 
cv2.waitKey(0)
