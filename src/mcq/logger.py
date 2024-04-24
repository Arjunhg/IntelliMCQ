import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #creating logger file #.log is the extention

log_path=os.path.join(os.getcwd(),"logs") #path where you want to save your log

os.makedirs(log_path,exist_ok=True) #making folder in path


LOG_FILEPATH=os.path.join(log_path,LOG_FILE) #making log file in folder


#Search python logger in docs
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


#using this logger file we can capture each and every info about execution. And in between we will be writing loggin.info for the part we want to log(capture, save, getInfo)