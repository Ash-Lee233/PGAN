
"""dataset"""
import os
from src.image_transform import pil_loader


class ImageDataset:
    """
    A dataset class adapted to the specificites of our YSL fashion dataset.
    It loads both the images and an attribute dictionary describing each image's
    attribute.
    """

    def __init__(self,
                 pathdb,
                 transform=None):
        """
        Args:
            - pathdb (string): path to the directory containing the images
            - transform (torchvision.transforms): a function object list to convert image to np array

        """
        self.totAttribSize = 0
        self.pathdb = pathdb
        self.transforms = transform
        imagesPaths = os.listdir(pathdb)
        self.listImg = [imgName for imgName in imagesPaths
                        if os.path.splitext(imgName)[1] in [".jpg", ".png"]]
        print("%d images found" % len(self))

    def __len__(self):
        return len(self.listImg)

    def __getitem__(self, idx):
        imgName = self.listImg[idx]
        imgPath = os.path.join(self.pathdb, imgName)
        img = pil_loader(imgPath)
        if self.transforms is not None:
            for transform in self.transforms:
                img = transform(img)
        return img, 1

    def getName(self, idx):
        return self.listImg[idx]
