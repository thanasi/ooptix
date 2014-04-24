########################
## ooptix.geometric
##
## thanasi
##
## April 2014
##
########################
import numpy as np


class GOptSys(object):

    def __init__(self):
        pass

    def __call__(self, image):
        pass

    def add(self, component, position):
        pass

    def remove(self, position):
        pass

    def calc_matrix(self):
        pass

    def calc_magnification(self):
        pass

    def calc_pps(self):
        pass

    def calc_fps(self):
        pass

    def update(self):
        pass

    def __repr__(self):
        pass


class Lens(object):

    def __init__(self, f, n=1.5):
        pass

class FreeSpace(object):

    def __init__(self, n=1):
        pass

class Mirror(object):

    def __init__(self, f):
        pass

class ObjectIn(object):

    def __init__(self):
        pass

class Ray(object):

    def __init__(self):
        pass