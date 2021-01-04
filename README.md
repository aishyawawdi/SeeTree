# Seetree Junior SW engineer task
In this assignment we implemented Flask -webserver that handles calculation of image statistics.
With the giving image we calculated different functions: min,max,mean,median and percentile.

## make sure that you have
* python
* Git


## Setup
Clone the repo and install the dependencies.
```bash
git clone https://github.com/aishyawawdi/SeeTree.git
```

## RUN using Flask

Open the Command Prompt and enter "SeeTree" folder.
To start the server, run the following:
```bash
py -m pip install -r requirements.txt
set FLASK_APP=SeeTree-task.py
python -m flask run 
```
Open https://127.0.0.0:5000 on your browser and start your trip in the website. 

## RUN using Dockerfile

Open the Command Prompt and enter "SeeTree" folder.
To start the web, run the following to create the image for the docker:
```bash
docker build -t seetree-task .
```
and then run the following to start the container:
```bash
docker run -d -p 5000:5000 seetree-task
```
Open https://127.0.0.0:5000 on your browser and start your trip in the website. 

## RUN using docker-compose 

 From your project directory, start up your application by running:   docker-compose up --build -d

## RUN using Kubernetes
you also can implement a deplpyment that contains our container image and its relevant service.

## Supported URLs
you can use those urls:
* http://127.0.0.1:5000/health
  that returns OK to any request.
* http://127.0.0.1:5000/stats/IMAGE_FILE_NAME/FUNC_NAME
  while IMAGE_FILE_NAME is the Image name and FUNC_NAME is your required function. 

## Explanation
this web will calculate FUNC_NAME on the pixels of given IMAGE_FILE_NAME and return the result.
 Supported FUNC_NAMES are:
1- min :                                                                                                      
returns Min value of pixles in the image.                                                                      
This relies on the histogram() method, and simply returns the low and high bins used.                          
2- max:                                                                                                        
returns Max value of pixles in the image.                                                                     
This relies on the histogram() method, and simply returns the low and high bins used.                         
3- mean:                                                                                                       
returns Average (arithmetic mean) pixel level in the image.                                                  
4- median:                                                                                                     
returns Median pixel level in the image.                                                                       
5-  pXXX where XXX is a percentile between 0...100 :                                                           
For example p10 is the 10th percentile of the image, p99 is the 99th percentile
returns a value that a certain percentage of a set of values (p%) is lower than it.                           

## Implementation
* For each function i chose to return html rather than Json for user comfort so he can have much more fun! 

* I calculated each function on the given image grayscale and not on the image itself, and that due to the     RGB image Composition; each RGB image has three channels: red, green, and blue . the function (min for example) relies on the histogram for each channel and computes the min value for each channel; but in the
assignment we asked to return the min value of the whole image, therefore i chose to work on the grayscale image.
also for the percentile function i didn't see meaning of working on the RGB image because the function returns 
the percntile according to comparition with other pixles values in one channel so it needs to be grayscale image!

* I have implemented my own error 404 handler,each for different purpose:                                     
1- if the image name is not exists on the server.                                                              
2- if the function name is wrong.                                                                            
3- if the url is not supported.                                                                               

* I wrapped everything in Class.

## Examples
1. Request to /stats/IMG_3.jpg/min responds with the correct min value in the
   image.

2. Request to /stats/IMG_5.jpg/blah responds with 404 error code.

3. Request to /stats/IMG_99.jpg/min responds with 404 error code.

4. Request to /stats/IMG_4.jpg/p10 responds with the 10'th percentile of the image.
   (assuming such image was not added to the bucket).

## multiple identical requests
in case of multiple identical requests (same image and same function) we can make it more efficient
by providing a Hash table (or DB) that stores each legal request by the user in it. so whenever the user request some request from the server we check first if the specific image and function are stored in the hash table; if so we return the stored data without the need to calculate it all over again. (in other words- caching like) 
