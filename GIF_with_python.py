import imageio.v3 as iio
import os 

filenames = ['img1.png' , 'img2.png']
images = [ ]

for filename in filenames :
    images.append(iio.imread(filename))
iio.imwrite('team.gif' , images , duration = 500 , loop = 0)
os.startfile("team.gif")
