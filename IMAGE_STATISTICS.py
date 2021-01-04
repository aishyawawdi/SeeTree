#import FILENAME
#EXAMPLE:
#import hello
#hello.my_function()
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

#from hello import my_function
#my_function()


import numpy as np               
from PIL import ImageStat

class IMAGE_STATISTICS:
        
    #takes an image in grayscale and return the min value
    def Min_value(self,img): 
        min_max = ImageStat.Stat(img).extrema #Min/max values of pixles in the image
        min_val=min_max[0][0]
        return min_val

    #takes an image in grayscale and return the max value
    def Max_value(self,img): 
        min_max = ImageStat.Stat(img).extrema #Min/max values of pixles in the image
        max_val=min_max[0][1]
        return max_val

    #Average (arithmetic mean) pixel level in the image.
    def Mean_value(self,img): 
        Mean_value = ImageStat.Stat(img).mean[0] 
        return Mean_value

    #Median pixel level in the image.
    def Median_value(self,img): 
        Median_value = ImageStat.Stat(img).median[0]
        return Median_value
    #n'th percentile of the image
    def percentile_value(self,img,p):
        numpydata = np.asarray(img) # convert PIL images into NumPy arrays 
        percentile= np.percentile(numpydata,p) # calculate n'th percentile of the image
        return percentile
        