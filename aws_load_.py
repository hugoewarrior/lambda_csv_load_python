
import os 
from os import path
import time
import subprocess

def check_for_file(file_path):
    e = path.exists(file_path)
    destination_bucket= str("s3://locationsbucket/")
    if e: 
        print("File is here "+ str(e))
        print("Uploading file...")
        subprocess.run("aws s3 mv "+file_path+" "+destination_bucket, shell=True, check=True)
        os.system("aws s3 ls "+destination_bucket)

    else: 
        print("File is not here mate "+ str(e))
        time.sleep(5)
        check_for_file(file_path)


def main():
    init_path = str(r"C:\Users\Hugo\Desktop\DevTools\Dojos\AWS_Lambda_and_file_management\location.csv")
    check_for_file(init_path)

if __name__== "__main__":
   main()