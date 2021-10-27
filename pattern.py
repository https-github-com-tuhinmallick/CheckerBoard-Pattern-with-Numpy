#Importing the python libraries
import numpy as np
import matplotlib.pyplot as plt

#Implementing the constructor to initialize the parameters
class Checker(object):
    def __init__(self, resolution, tile_size):
        self.resolution = resolution    #integer resolution that defines the number of pixels in each dimension
        self.tile_size = tile_size      #integer tile size that defines the number of pixel an individual tile has in each dimension
        self.output = np.zeros([resolution, resolution])    #to store the pattern

#To create the checkerboard pattern as a numpy array
    def draw(self):
        # In order to avoid truncated checkerboard patterns, we make sure resolution is evenly dividable  by 2· tile size.
        if (self.resolution % (2 * self.tile_size) == 0):
            # self.output = np.tile(np.array([[0, 1], [1, 0]]), (self.size, self.size))
            re = np.zeros([self.tile_size, self.tile_size])
            ro = np.ones([self.tile_size, self.tile_size])
            opo = np.concatenate((re, ro), axis=1)
            opi = np.concatenate((ro, re), axis=1)
            op = np.concatenate((opo, opi), axis=0)
            fact = self.resolution / (2 * self.tile_size)
            fact = int(fact)
            self.output = np.tile(op, (fact, fact))
            fin = np.copy(self.output)
        else:
            assert "Truncation Error"

        return fin
    # shows the checkerboard pattern
    def show(self):
        plt.imshow(self.output, cmap='gray')    #to display a grayscale image,cmap=gray is used
        plt.show()

# to implement is a binary circle with a given radius at a specified position
class Circle(object):
    def __init__(self, resolution, radius, position):
        self.res = resolution           #integer resolution that defines the number of pixels in each dimension
        self.rad = radius               #integer resolution, an integer radius that describes the radius of the circle
        self.pos_x = position[0]        #x-coordinate of the circle center
        self.pos_y = position[1]        #y-coordinate of the circle center
        self.output = np.zeros([resolution, resolution])        #to store the pattern

    def draw(self):
        X = np.array(np.linspace(0, self.res, self.res), dtype='int')
        Y = np.array(np.linspace(0, self.res, self.res), dtype='int')
        #np.meshgrid creates a coordinate grid for the respective dimension
        a, b = np.meshgrid(X, Y, indexing='xy')
        # Circle equation is (x-h)**2 + (y-k)**2 - r**2 =0
        self.output = (((a - self.pos_x) ** 2) + ((b - self.pos_y) ** 2) - (self.rad ** 2)) < 0

        return np.copy(self.output)      #returns a copy


    # shows the circle
    def show(self):
        plt.imshow(self.output, cmap='gray')        #to display a grayscale image,cmap=gray is used
        plt.show()

# to implement is an RGB color spectrum
class Spectrum(object):
    def __init__(self, resolution):
        self.res = resolution       #integer resolution that defines the number of pixels in each dimension
        self.output = np.zeros([resolution, resolution, 3])     #to store the color spectrum
# to create the spectrum as a numpy array
    def draw(self):
        # linspace creates an array by creating as many elements
        # as numelements between start and the stop point
        self.output[:, :, 0] = np.tile(np.linspace(0, 1, self.res), (self.res, 1))
        self.output[:, :, 1] = np.transpose(np.tile(np.linspace(0, 1, self.res), ( self.res, 1)))
        self.output[:, :, 2] = np.tile(np.linspace(1, 0, self.res), (self.res, 1))

        return np.copy(self.output)     #returns a copy

    # shows the e RGB spectrum scheme
    def show(self):
        plt.imshow(self.output)     #to display a grayscale image,cmap=gray is used
        plt.show()




