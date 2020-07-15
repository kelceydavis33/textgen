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
	bols = []
	nfs = []
	rests = []
	afrs = []
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
			bols.append(bolometer)
			nfs.append(nom_freq)
		for ochan in range( 1, len(data['overbiased'])):#Grab the relavent info
			try:
				resist = data['overbiased'][ochan]['R']
				act_freq = data['overbiased'][ochan]['freq']#Define the data
			except:
				resist = np.nan
				act_freq = np.nan
			rests.append(resist)
			afrs.append(act_freq)
		f.close()
	pd_data = {'Name':[np.array(bols)],'Nominal Frequency':[np.array(nfs)],'Actual Frequency': [np.array(afrs)],'Resistance':[np.array(rests)]}#Create the dataframe
	df = pd.DataFrame(pd_data, columns = ['Name', 'Nominal Frequency','Actual Frequency','Resistance'])
	df.to_csv(text_file_directory + '{}.txt'.format(folder), header = True, index = False)