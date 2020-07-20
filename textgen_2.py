import os
import pickle as pkl
import glob
import pandas as pd
import numpy as np#Create a list of all file folders in current directory
input_folders = input("What is the absolute path to the folder containing the data files? ")#Get the names of all the folders
folders = os.listdir(input_folders)#Create a directory to store the text files
text_file_directory = input("Where should the output text files be saved? ")#Look at each indiviual folder
skipped_files = 0
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
        try:
            data = pkl.load(f)#Loop over the channels
            bstr = False
            f.close()
        except:
            f.close()
            f = open(fname,'rb')
            data = pkl.load(f,encoding='bytes')
            bstr = True
            f.close()
        if bstr == False:
            for schan in data['subtargets']:#Grab the relavent info
                #try:                    # by looping over keys in schan, these values will always be there
                bolometer = data['subtargets'][schan]['bolometer']
                nom_freq = data['subtargets'][schan]['frequency']
                #except:
                #	bolometer = np.nan
                #	nom_freq = np.nan
                #for ochan in range( 1, len(data['overbiased'])):#Grab the relavent info
                try:                     # need to loop over schan still, so that the lists end up the same length
                    resist = data['overbiased'][schan]['R']
                    act_freq = data['overbiased'][schan]['freq']#Define the data
                except:
                    resist = 'NaN'         # make this NaN string so it gets written to text file properly
                    act_freq = 'NaN'
                bols.append(bolometer)
                nfs.append(nom_freq)
                rests.append(resist)
                afrs.append(act_freq)
        elif bstr == True:
            for schan in data[b'subtargets']:#Grab the relavent info
                bolometer = data[b'subtargets'][schan][b'bolometer']
                nom_freq = data[b'subtargets'][schan][b'frequency']
                try:                     # need to loop over schan still, so that the lists end up the same length
                    resist = data[b'overbiased'][schan][b'R']
                    act_freq = data[b'overbiased'][schan][b'freq']#Define the data
                except:
                    resist = 'NaN'         # make this NaN string so it gets written to text file properly
                    act_freq = 'NaN'
                bols.append(bolometer)
                nfs.append(nom_freq)
                rests.append(resist)
                afrs.append(act_freq)





    pd_data = {'Name':bols,'Nominal Frequency':nfs,'Actual Frequency': afrs,'Resistance':rests}#Create the dataframe
    df = pd.DataFrame(pd_data, columns = ['Name', 'Nominal Frequency','Actual Frequency','Resistance'])
    df.to_csv(text_file_directory + '{}.txt'.format(folder), header = True, index = False)
