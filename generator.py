import os.path
import json
import numpy as np
import skimage.transform
import matplotlib.pyplot as plt


# In this exercise task you will implement an image generator.
# Generator objects in python are defined as having a next function.
# This next function returns the next generated object.
# In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:

    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle

        label_file = open(label_path)
        self.labels_dict = json.load(label_file)

        self.data_files = os.listdir(file_path)

        if self.shuffle:
            np.random.shuffle(self.data_files)
        else:
            self.data_files.sort()

        self.idx = 0
        self.epoch_counter = 0
     

    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        # TODO: implement next method
        images = []      #initializes an empty list of images
        labels = []      #initializes an empty list of labels

        batch_files = self.data_files[self.idx: self.idx + self.batch_size]
        #if shuffle = true, then it will shuffle the Dataset
        if self.shuffle:
            np.random.shuffle(self.data_files)     #function to shuffle the Dataset 
        # If the last batch is smaller than batch size, then reuse initial images. 
        if len(batch_files) < self.batch_size:
            self.idx = self.batch_size - len(batch_files)
            batch_files.extend(self.data_files[:self.idx])
            self.epoch_counter += 1       #counter to estimate the current epoch
        else:
            self.idx = self.idx + self.batch_size

        for img_file in batch_files:
            img = np.load(self.file_path + img_file)
            # Resize images, if needed
            if img.shape != self.image_size:
                img = skimage.transform.resize(img, self.image_size)
            if np.random.choice([True, False]):
                img = self.augment(img)
            lbl = self.labels_dict[img_file.split('.')[0]]
            images.append(img)
            labels.append(lbl)

        return np.array(images), np.array(labels)

    def augment(self, img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        # TODO: implement augmentation function

        if self.rotation:
            # Rotate
            img = np.rot90(img, np.random.choice([1, 2, 3]))

        if self.mirroring:
            # Mirror
            img = np.flip(img, 1)

        return img

    def current_epoch(self):
        # return the current epoch number
        return self.epoch_counter

    def class_name(self, x):
        # This function returns the class name for a specific input
        # TODO: implement class name function
        return self.class_dict[x]

    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        # TODO: implement show method
        images, labels = self.next()

        # TODO: Decide number of rows and columns
        plot_r = 3
        plot_c = 4

        fig = plt.figure()
        for idx, (img, lbl) in enumerate(zip(images, labels)):
            sp = fig.add_subplot(plot_r, plot_c, idx + 1)
            sp.imshow(img)
            sp.title.set_text(self.class_name(lbl))

        plt.show()
© 2021 GitHub, Inc.
Terms
Privacy
