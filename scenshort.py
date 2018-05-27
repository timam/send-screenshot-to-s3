import pyscreenshot as ImageGrab
import time
import boto3

#Importing credentials 
from secrets import *


if __name__ == "__main__":
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ImageGrab.grab_to_file(timestr +'my.png')
    image_name = timestr +'my.png'

    data = open(image_name, 'rb')

    s3 = boto3.resource(
        's3',
        aws_access_key_id=gimme_aws_access_id(),
        aws_secret_access_key=gimme_aws_secret_access_key()
    )
    s3.Bucket('screenshot-python').put_object(Key=image_name, Body=data)

    print ("Done")
