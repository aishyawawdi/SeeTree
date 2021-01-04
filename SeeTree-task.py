#from my_file import myClass
import requests
from flask import Flask,Response,render_template
from PIL import Image,ImageOps
import numpy as np 
import IMAGE_STATISTICS as imgstat
import time
import sys
app = Flask(__name__)

Dict_request={}


#check if a URL of an image is up and exists in the bucket
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


# app name 
@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e): 
  
# defining function 
  return render_template("404.html"), 404


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/health',methods=['GET'])
def func():
    return render_template('ok.html'),200


@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>',methods=['GET'])
def get_result(IMAGE_FILE_NAME,FUNC_NAME):
    start_time = time.time()

    if IMAGE_FILE_NAME in Dict_request.keys():
        if FUNC_NAME in Dict_request[IMAGE_FILE_NAME].keys():
            elapsed_time = time.time() - start_time
            print("from the dict: "+str(elapsed_time), file=sys.stdout)
            return render_template('stats_index.html',func=FUNC_NAME,img_url=Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"],img_name=IMAGE_FILE_NAME, value=Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"],describtion=Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"])


    url = 'https://storage.googleapis.com/seetree-demo-open/{}'.format(IMAGE_FILE_NAME) #image url
    if not is_url_image(url):          #if the image doesn't exists
        return render_template('img_404.html'),404 

    input_image=Image.open(requests.get(url, stream=True).raw)
    gray_image = ImageOps.grayscale(input_image) #Convert RGB Image to Grayscale image

    
    if FUNC_NAME =='min': 
        min_val=imgstat.IMAGE_STATISTICS.Min_value(imgstat,gray_image) 
        elapsed_time = time.time() - start_time
        print("regular time: "+str(elapsed_time),file=sys.stdout)
        Dict_request[IMAGE_FILE_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=url
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"]=min_val
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]="This function calculates the Min value of pixels in the giving image."

        return render_template('stats_index.html',func=FUNC_NAME,img_url=url,img_name=IMAGE_FILE_NAME, value=min_val,describtion="This function calculates the Min value of pixels in the giving image.")
    
    
    elif FUNC_NAME =='max':
        max_val=imgstat.IMAGE_STATISTICS.Max_value(imgstat,gray_image)
        elapsed_time = time.time() - start_time
        print("regular time: "+str(elapsed_time),file=sys.stdout)
        Dict_request[IMAGE_FILE_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=url
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"]=max_val
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]="This function calculates the Max value of pixels in the giving image."
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=max_val,describtion="This function calculates the Max value of pixels in the giving image.")

    elif FUNC_NAME =='mean':
        Mean_value=imgstat.IMAGE_STATISTICS.Mean_value(imgstat,gray_image)
        elapsed_time = time.time() - start_time
        print("regular time: "+str(elapsed_time),file=sys.stdout)
        Dict_request[IMAGE_FILE_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=url
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"]=Mean_value
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]="This function calculates the Average pixel level in the giving image."
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=Mean_value,describtion="This function calculates the Average pixel level in the giving image.")

    elif FUNC_NAME =='median':
        Median_value=imgstat.IMAGE_STATISTICS.Median_value(imgstat,gray_image)
        elapsed_time = time.time() - start_time
        print("regular time: "+str(elapsed_time),file=sys.stdout)
        Dict_request[IMAGE_FILE_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]={}
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=url
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"]=Median_value
        Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]="This function calculates the Median pixel level in the giving image."
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=Median_value,describtion="This function calculates the Median pixel level in the giving image.")

    elif FUNC_NAME[0]=='p' and FUNC_NAME[1:].isnumeric():
        if int(FUNC_NAME[1:])>=0 and int(FUNC_NAME[1:])<=100:
            percentile=imgstat.IMAGE_STATISTICS.percentile_value(imgstat,gray_image,int(FUNC_NAME[1:]))
            elapsed_time = time.time() - start_time
            print("regular time: "+str(elapsed_time),file=sys.stdout)
            Dict_request[IMAGE_FILE_NAME]={}
            Dict_request[IMAGE_FILE_NAME][FUNC_NAME]={}
            Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["img_url"]=url
            Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["value"]=percentile
            Dict_request[IMAGE_FILE_NAME][FUNC_NAME]["describtion"]="This function calculates the required Percentile of the giving image."
            return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=percentile,describtion="This function calculates the required Percentile of the giving image.")

        else:                                                # the percentile is NOT between 0..100 (function doesn't exists)
            return render_template('func_404.html'),404     

    else:  # the function doesn't exists
         return render_template('func_404.html'),404

    

        
        
    


     
    

    














if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)



