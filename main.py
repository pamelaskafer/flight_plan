#!/usr/bin/python

scale = float(input("Scale: "))
cam_focus_distance = float(input("Camera focus distance: "))
photo_size = float(input("Photo size: "))
area = float(input("Area: "))
plane_speed = float(input("Plane speed: "))
long_cover = float(input("Long cover: "))
side_cover = float(input("Side cover: "))

def getWidth():
	photo_size_m = photo_size / 100
	width = scale * photo_size_m
	return width	

def planeHeight():
	cam_focus_m = cam_focus_distance / 1000
	ph = scale * cam_focus_m 
	return ph

def airbase(long_cover):
	ab = (1 - long_cover) * getWidth()
	return ab

def bandDistance(side_cover):
	bd = (1 - side_cover) * getWidth()
	return bd

def usefulArea():
	ua = (airbase(long_cover) * bandDistance(side_cover)) / 10000
	return ua

def totalPhotos():
	tp = area / usefulArea()
	return tp

def photoInterval():
	pi = airbase(long_cover) / (plane_speed / 3.6)
	return pi

print("#############  RESULT ################")

# Getting plane height
planeH = planeHeight()
print("Plane height: %.0f" % planeH + "m")

# Getting airbase
aBase = airbase(long_cover)
print("Airbase: %.0f" % aBase + "m")

# Getting bandDistance
bDistance = bandDistance(side_cover)
print("Band distance: %.0f" % bDistance + "m")

# Getting usefulArea
uArea = usefulArea()
print("Useful Area: %.2f" % uArea + "ha")

# Getting totalPhotos
tPhotos = totalPhotos()
print("Total of Photos: %.0f" % tPhotos + " photos")

# Getting photoInterval
pInterval = photoInterval()
print ("Photo Interval: %.0f" % pInterval + "s")
