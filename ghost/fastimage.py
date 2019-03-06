#!/usr/bin/env python3

"""
Stanford CS106AP FastImage module -
access image data as tuples.

Create image:
  image = FastImage.blank(400, 200)   # create new image of size
  image = FastImage.file('foo.jpg')   # create from file

Access size
  image.width, image.height

Get pix at x,y
  pix = image.get_pix(x, y)
  # pix is RGB tuple like (100, 200, 0)

Set pix at x,y
  image.set_pix(x, y, pix)   # set data by tuple also

Show image on screen
  image.show()

Example use - makes big yellow image
(this same code is in main() in this file).
...

    image = FastImage.blank(500, 300)
    for y in range(image.height):
        for x in range(image.width):
            image.set_pix(x, y, (255, 255, 0))
    image.show()
"""

# If this line fails, "Pillow" needs to be installed
from PIL import Image


class FastImage(object):
    def __init__(self, width=None, height=None, filename=None):
        if filename:
            self.pil_image = Image.open(filename)
            if (self.pil_image.mode != 'RGB'):
                raise Exception('Image file is not RGB')
            self._filename = filename # hold onto
        elif width:
            self.pil_image = Image.new("RGB", (width, height), (255, 255, 255))
        else:
            raise Exception('Creating FastImage requires size or filename')
        self.px = self.pil_image.load()
        size = self.pil_image.size
        self._width = size[0]
        self._height = size[1]

    @classmethod
    def blank(cls, width, height):
        """Create blank image of the given size."""
        return FastImage(width=width, height=height)

    @classmethod
    def file(cls, filename):
        """Create imaeg loaded from the given file."""
        return FastImage(filename=filename)

    @property
    def width(self):
        """Get width in pixels."""
        return self._width

    @property
    def height(self):
        """Get height in pixels."""
        return self._height

    def get_pix(self, x, y):
        """Get pix RGB tuple (200, 100, 50) for the given x,y."""
        return self.px[x, y]

    def set_pix(self, x, y, pix):
        """Set the given pix RGB tuple into the image at the given x,y."""
        self.px[x, y] = pix

    def show(self):
        """Displays the image using an external utility."""
        self.pil_image.show()

    def save_width(self, new_width):
        """
        Create a resized version of the image to the given width
        and save it as a new file.
        Used to create assignment files.
        """
        factor = new_width / self._width
        resized = self.pil_image.resize((new_width, int(self._height * factor)), Image.BILINEAR)
        new_name = self._filename[:-4] + '-' + str(new_width) + '.jpg'
        resized.save(new_name)


def test_main():
    """
    Make a big yellow image - demonstrates simple use of FastImage.
    """
    image = FastImage.blank(500, 300)
    print(image)
    for y in range(image.height):
        for x in range(image.width):
            image.set_pix(x, y, (255, 255, 0))
    image.show()


if __name__ == '__main__':
    test_main()
