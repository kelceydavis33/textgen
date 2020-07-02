#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:26:52 2020

@author: kelcey
"""

#name, nominal_freq, actual_freq, resistance
#change 2 inputs, where plots are and where to save
#


import os
import pickle as pkl
import glob
import pandas as pd
import numpy as np

#Create a list of all file folders in current directory
input_folders = input("What is the absolute path to the folder containing the data files? ")#os.listdir(os.curdir)  
#Get the names of all the folders
folders = glob.glob(input_folders)
#Create a directory to store the text files
os.mkdir(working_directory +'/text_files')
#Note the name of the directory to save the files
text_file_directory = input("Where should the output text files be saved? ")#(working_directory + '/' + 'text_files/')

#Look at each indiviual folder
for folder in folders:
    #grab each data file within the directory
	data_files = glob.glob(folders + '/' + folder +  '/' + 'IceCrate*_OUTPUT.pkl')
    #Print the iteration in the list and clear the previous one so user can keep track
	os.system('clear')
	print("Generating text file {} of {}".format(folders.index(folder), len(folders))
	#Loop over teh data files
    for fname in data_files:
        #Open the file
		f = open(fname, 'rb')
        #Load the pickle data
		data = pkl.load(f)
        #Loop over the channels 

		for chan in range( 1, len(data['subtargets']))
            #Grab the relavent info
			bolometer = data['subtargets'][chan]['bolometer']
			nom_freq = data['subtargets'][chan]['frequency']
			resist = data['overbiased'][chan]['R']
			act_freq = data['overbiased'][chan]['freq']
            
            
            
            #Define the data
			pd_data = {'Name':[bolometer], 
                       'Nominal Frequency':[nom_freq], 
                       'Actual Frequency': [act_freq], 
                       'Resistance': [resist]}
            #Create the dataframe
			df = pd.DataFrame(data, columns = ['Name', 
                                               'Nominal Frequency',
                                               'Actual Frequency',
                                               'Resistance'])
            #Write the data out to a text file
			np.savetext(text_file_directory + '{}.txt'.format(folder), df.values, delimiter = "\t", header = "name\tnom_freq\tctfreq\tresist")
            #Close the file 
			f.close()