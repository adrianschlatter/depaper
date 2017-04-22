"""
depaper package
+++++++++++++++
"""

from skimage.filters import threshold_otsu
from skimage.exposure import rescale_intensity
from numpy import median


def depaper(img):
    """Clean grayscale image of scanned paper"""

    if img.ndim != 2:
        raise TypeError('depaper currently only works on grayscale images')

    thresh = threshold_otsu(img)
    mask = img < thresh
    blackPnt = median(img[mask])
    whitePnt = median(img[~mask])
    return(rescale_intensity(img, in_range=(blackPnt, whitePnt)))


if __name__ == '__main__':
    import matplotlib.pyplot as pl
    img = pl.imread('pages_01.png')
    depapered = depaper(img)
    pl.imsave('test.png', depapered, vmin=0, vmax=1, cmap=pl.cm.gray)
