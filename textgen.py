import os
import pickle as pkl
import glob
import pandas as pd
import numpy as np#Create a list of all file folders in current directory
input_folders = input("What is the absolute path to the folder containing the data files? ")#Get the names of all the folders
folders = os.listdir(input_folders)#Create a directory to store the text files
text_file_directory = input("Where should the output text files be saved? ")#Look at each indiviual folder
for folder in folders:#grab each data file within the directory
	data_files = glob.glob(input_folders + folder +  '/data/' + 'IceCrate*_OUTPUT.pkl')#Print the iteration in the list and clear the previous one so user can keep track
	os.system('clear')
	print("Generating text file {} of {}".format(folders.index(folder)+1, len(folders)))#Loop over teh data files
	for fname in data_files:#Open the file
		f = open(str(fname), 'rb')#Load the pickle data
		data = pkl.load(f)#Loop over the channels 
		for schan in range( 1, len(data['subtargets'])):#Grab the relavent info
			try:
				bolometer = data['subtargets'][schan]['bolometer']
				nom_freq = data['subtargets'][schan]['frequency']
			except:
				bolometer = np.nan
				nom_freq = np.nan
		for ochan in range( 1, len(data['overbiased'])):#Grab the relavent info
			try:
				resist = data['overbiased'][ochan]['R']
				act_freq = data['overbiased'][chan]['freq']#Define the data
			except:
				resist = np.nan
				act_freq = np.nan
			pd_data = {'Name':[bolometer],'Nominal Frequency':[nom_freq],'Actual Frequency': [act_freq],'Resistance': [resist]}#Create the dataframe
			df = pd.DataFrame(data, columns = ['Name', 'Nominal Frequency','Actual Frequency','Resistance'])#Write the data out to a text file
			np.savetext(text_file_directory + '{}.txt'.format(folder), df.values, delimiter = "\t", header = "name\tnom_freq\tctfreq\tresist")#Close the file 
			f.close()
