# script to merge largest cell from a selection of rasters with identical geometry
# Calum Bradbury 27/10/19

import csv
import pandas as pd
import os
import glob
import linecache
import sys

###############################
##CHANGE THESE VARIABLES ONLY##
###############################

#target directory containing the source rasters
#two \ between each file level, two at the end
target = 'C:\\Users\\calum\\Desktop\\Caesar2019\\'

#output file name. Must include extension such as .txt
output = 'output2.txt'

################################
################################
################################

#index raster. Not really neccesary but make handling easier
index_raster = os.path.join(target,"index.txt")

#index iteration controller. Also sets number of lines to skip
x_i = 1

#logic to set up output file as an empty text file
with open(target+output,'w') as writeLine:
  print("reset output file")

#getting all source rasters as a list
rasterList = glob.glob(target+'water*.txt')
  
#function to append output line by line in target directory
def lineWriter(inputText):  
  #print(inputText)
  with open(target+output,'a') as writeLine:
    writeLine.write(inputText)
    
#function to get line of raster at defined index and return as list
def getRasterLine(inputRaster,index):
  #does this linecache funtion work properly?
  rasterLine = linecache.getline(inputRaster,index)
  rasterLine = rasterLine.replace(' \n','')
  #set deliminater
  rasterLineList = rasterLine.split(" ")
  return rasterLineList

#function to read list of lists into pandas dataframe and return list of column maximums
def toDataFrame(list_of_lists):
  data_frame = pd.DataFrame(list_of_lists)
  max_series = data_frame.max()
  max_list = max_series.tolist()
  return max_list
    
#function to build pandas object from specific line in each raster
def temporaryRaster(index):
  temporary_list = []
  for raster in rasterList:
    #appending list from each raster
    temporary_list.append(getRasterLine(raster,index))
    
  maximum_list = toDataFrame(temporary_list)
  # need some logic here to convert list to string with appropriate deliminater
  maximum_string = ''
  for item in maximum_list:
    maximum_string = maximum_string+str(item)
    maximum_string = maximum_string+' '
    #print(maximum_string) 
  maximum_string = maximum_string+'\n'
  lineWriter(maximum_string)



#main script
#driven line by line by the index raster
with open(target+'index.txt','r') as indexRaster:
  for line in indexRaster:
    if x_i < 7:
      #copying ASCII information to output file
      lineWriter(line)
    else:
      print("at index numer ",x_i)
      temporaryRaster(x_i)
    x_i += 1
