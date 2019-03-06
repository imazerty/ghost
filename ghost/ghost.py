#!/usr/bin/env python3

"""
Stanford CS106AP Ghost Project
"""

import os
import sys

# This line imports FastImage for use here
# This depends on the Pillow package
from fastimage import FastImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    """
    result = 0
    for i in range(len(pix1)):

        result +=  (pix1[i] - pix2[i]) ** 2
    return result
    pass

def average(pixs):
    """
    Given a list of 3 or more pix, returns the average pix.
    """

    summingX = summingY = summingZ = 0
    for i in range(len(pixs)):
        summingX += pixs[i][0]
        summingY += pixs[i][1]
        summingZ += pixs[i][2]
    avX = int (summingX / len(pixs))
    avY = int (summingY / len(pixs))
    avZ = int (summingZ / len(pixs))
    return avX , avY, avZ


    pass

def best_pix_compare(pixs, average):
    """
    Given the list of pixs and average, returns
    the tuple (best pix, nbre) .
    """
    if len(pixs) > 0:
        min = pix_dist2(pixs[len(pixs) - 1 ],  average)

        index = len(pixs) - 1
        for i in range(len(pixs) - 1):
            pd = pix_dist2(pixs[i],  average)
            if pd < min:
                min = pd
                index = i

        return pixs[index]


    else:
        return "no pixs entered"
    pass



def best_pix(pixs):
    """
    Given a list of 3 or more pix, returns the best pix.
    """
    avg = average(pixs)
    result = best_pix_compare(pixs, avg)
    return result

    pass



def solve(images):
    """
    Given a list of image objects, compute and show
    a Ghost solution image based on these images.
    There will be at least 3 images and they will all be
    the same size.
    """




    height =  images[0].height
    width = images[0].width
    imagResul = FastImage.blank(width, height)
    for x in range(width):
        for y  in range(height):
            pixs = []
            for i in range(len(images)):
                image = images[i]
                pix = image.get_pix(x, y)
                pixs.append(pix)
            bestXY = best_pix(pixs)
            imagResul.set_pix(x, y, bestXY)
    imagResul.show()


    pass


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    result = []
    for fname in os.listdir(dir):
        if fname.endswith('.jpg'):
            result.append(os.path.join(dir, fname))
            
    return result


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = FastImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
