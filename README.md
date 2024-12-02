# Assignment 5

For the exercises of lecture 5, the libraries json, pickle, and pandas are required. Additionally, modules like datetime and re are used for specific operations. Run the following commands at the beginning of the script to ensure necessary imports:
import json  
import pickle  
import pandas as pd  
from datetime import datetime  
import re  

# Exercises Outline
1. Identify the number of annotations present within session_4 folder per month and year using the library os to access the files and datetime library to extrapolate the date and time portion of thr file's name. Then highlight which month has the largest number of annotations.
2. Create a dictionary with each key representing the month while the value is a list of all annotations with their date corresponding the the key (month).
  a. save the dictionary in json format and load it again to ensure a correct storage.
   b. save the dictionary in pickle format and load it again to ensure a correct storage.
   c. Create a new dictionary where for each annotation the key is the name and date as a datetime object.
3. Print all annotations from oldest to newest based on the datetime portion of the file's name for all annotations in the second half of 2024. 
