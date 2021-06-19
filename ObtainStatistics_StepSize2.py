
############################################################################################################
 #### Written by: Asa'd Mustafa As'ad
 #### Latest Update: April 2021
 #### Link to the research project this script was used in:
 #### https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1198A/abstract
 #### Purpose of the code: Obtain the needed statistical results from the files produced by ASAD program


 #### Input files:
 #### The input files are the ones obtained after runing the ASAD program.
    ### The file names of these files vary because ASAD program allow the user to choose the file name.
    ### The file names use in this code are: 68.txt / 69.txt / 70.txt ... etc.
    ### The lines below show the content on one of the files:
#Model name					Minimum Age	Minimum Reddening	Test Statistical Value
#output70.06_90_16.txt_68_msg_MIST_Zm04.txt		71.02		0.0			0.211285097902
#output70.06_90_27.txt_68_msg_MIST_Zm04.txt		70.06		0.0			0.13244364346
#output70.06_90_10.txt_68_msg_MIST_Zm04.txt		70.06		0.0			0.132346226474
#output70.06_90_0.txt_68_msg_MIST_Zm04.txt		71.03		0.0			0.137741354498
#output70.06_90_6.txt_72_msg_MIST_Zm04.txt		71.02		0.0			0.331198332867

 #### Intermediate files:
 ### For each of the input files, this script produces the following intermediate-step files:
     ### A)  68.dat / 69.dat / 70.dat (remove extra lines)
     ### B)  68_new.txt / 69_new.txt / 70_new.txt (keep numbers only)
     ### C)  68_Stat.txt / 69_Stat.txt / 70_Stat.txt
 ### The lines below show the content on one of the files:
 ### 68.dat:
 ### output70.06_90_16.txt_68_msg_MIST_Zm04.txt		71.02		0.0			0.211285097902
 ### output70.06_90_27.txt_68_msg_MIST_Zm04.txt		70.06		0.0			0.13244364346
 ### output70.06_90_10.txt_68_msg_MIST_Zm04.txt		70.06		0.0			0.132346226474

 ### 68_new.txt:
 ### 6.8 7.0 60 90 16 6.8 7.1 20
 ### 6.8 7.0 60 90 27 6.8 7.0 60
 ### 6.8 7.0 60 90 10 6.8 7.0 60

 ### 68_Stat.txt:
 ### 6.8 7.0 0 50 0.6 1.08 0.4 1.5 -0.6 0 25
 ### 6.8 7.0 0 60 1.1 1.15 0.9 2.0 -0.2 0 17
 ### 6.8 7.0 0 70 1.4 1.30 1.2 2.5 -0.1 0 15

 #### Output files:
 ### This script produces the following files:
    ###    StepSize2_10_Stat.txt / StepSize2_20_Stat.txt / StepSize2_30_Stat.txt ..etc

 ### The lines below show the content on one of the files (StepSize2_10_Stat.txt):
### 6.8 7.0 10 50 0.7 0.98 0.5 1.5 -0.5 6 23
### 6.9 7.1 10 50 0.7 0.85 0.5 1.3 -0.4 15 21
### 7.0 7.2 10 50 0.5 0.46 0.3 0.7 -0.2 6 15
### 7.1 7.3 10 50 0.6 0.78 0.4 1.2 -0.4 12 15
### 7.2 7.4 10 50 0.7 0.99 0.5 1.5 -0.4 11 21

###########################################################################################################





# Load required packages
import os
import pandas as pd
import numpy as np

################################################################################
######################### Remove extra lines from files ########################

for root, dirs, files in os.walk ("."):
    for Grand_File_TXT in files:
        if ".txt" in Grand_File_TXT: # 68.txt
            Grand_File_TXT_Name = Grand_File_TXT.split (".") # 68.txt
            Grand_Age1 = Grand_File_TXT_Name [0] # 68
            Grand_Age2 = str (int (Grand_Age1) + 2) # 70

            Input_Grand_TXT = open (Grand_File_TXT, "r")
            Output_Grand_TXT = open (Grand_Age1 + ".dat", "w")

            for line in Input_Grand_TXT:
                if line.startswith ("output" + Grand_Age2):
                    Output_Grand_TXT.write (line) # 68.txt
            Input_Grand_TXT.close ( )
            Output_Grand_TXT.close ( )

################################################################################
###################### Convert fles into numbers only format ###################

df_all = pd.DataFrame (columns = None) # Create empty dataframe (table)

for root, dirs, files in os.walk ("."):
    for Grand_File_DAT in files:
        if ".dat" in Grand_File_DAT: # 68.dat
            Grand_File_DAT_Name = Grand_File_DAT.split (".") # 68.dat
            Grand_Age_1 = Grand_File_DAT_Name [0] # 68
            Grand_Age_2 = str (int (Grand_Age_1) + 2) # 70
            Output_Grand_New_TXT = Grand_Age_1 + "_new.txt"

            df = pd.read_csv (Grand_File_DAT, engine = 'python', header = None, delim_whitespace = True)
            col1 = df [0] # output70.06_90_16.txt_68_msg_MIST_Zm04.txt
            col2 = df [1] # 71.02

            col11 = col1.astype (str).str.split ("_", expand = True)            # output70.06 90 16.txt 68 msg MIST Zm04.txt
            col11_0 = col11 [0].astype (str).str.split (".", expand = True)     # output70 06
            col11_0_1 = col11_0 [0].astype (str).str.split ("t", expand = True) # ou pu 70
            inp_age2 = col11_0_1 [2].astype (int) * 0.1                         # 7.0 # We then take only the integer part of that float and divide by 10

            new_age = inp_age2 - 0.2                                            # 6.8 # Add a new column

            inp_age1 = col11_0 [1].astype (int) * 10                            # 06 * 10 = 60

            inp_age0 = col11 [1]                                                # 90

            col11_2 = col11 [2].astype (str).str.split (".", expand = True)     # 16 txt
            inp_age_3 = col11_2 [0]                                             # 16

            inp_age_44 = col11 [3].astype (int) * 0.1                           # 6.8

            col22 = col2.astype (str).str.split (".", expand = True)            # 71 02
            inp_age4 = col22 [0].astype (int) * 0.1                             # 7.1

            inp_age3 = col22 [1].astype (int) * 10                              # 02 * 10 = 20

            df_all = pd.concat ([new_age.round (1), inp_age2.round (1), inp_age1, inp_age0, inp_age_3, inp_age_44.round (1), inp_age4.round (1), inp_age3], axis=1)   # 7.0 7.2 06 90 16 6.8 7.1 20
            df_all.to_csv (Output_Grand_New_TXT, sep = " ", header = None, index = None, mode = "w")

            ####################################################################
            ############################ Clean Data ############################

            df_SN = pd.read_csv (Output_Grand_New_TXT, engine = 'python', header = None, delim_whitespace = True)

            x = len (df_SN.columns)
            y = len (df_SN.columns) + 1
            z = len (df_SN.columns) + 2

            Temp_5 = df_SN.iloc [ : , 5]
            Temp_6 = df_SN.iloc [ : , 6]
            Temp_7 = df_SN.iloc [ : , 7]
            Temp_77 = 100 - df_SN.iloc [ : , 7]

            df_SN [x] = np.where (df_SN.iloc [ : , 5] > df_SN.iloc [ : , 6], Temp_6, Temp_5) # Add a new column at the end based on a condition (when age 1 > age 2 then flip them)
            df_SN [y] = np.where (df_SN.iloc [ : , 5] > df_SN.iloc [ : , 6], Temp_5, Temp_6) # Add a new column at the end based on a condition (when age 1 < age 2 then do not flip them)
            df_SN [z] = np.where (df_SN.iloc [ : , 5] > df_SN.iloc [ : , 6], Temp_77, Temp_7) # Add a new column at the end based on a condition (when age 1 > age 2 then flip the fraction value)

            df_SN_Sorted = df_SN.sort_values (by = [df_SN.columns [4]]) # Sort df_SN dataframe based on the sequence number (0-29)
            df_SN_Sorted.drop (df_SN_Sorted.iloc [:, 5:8], inplace = True, axis = 1) # Remove multiple columns (5, 6 and 7)

            ### Delete rows that has the identical values
            df_SN_Sorted.drop_duplicates (subset = [df_SN_Sorted.columns [0], df_SN_Sorted.columns [1], df_SN_Sorted.columns [2], df_SN_Sorted.columns [3], df_SN_Sorted.columns [4]], inplace = True)

            ####################################################################
            ############## Calculate mean and standard deviation ###############
            #################### Find numbers of recovery ######################

            #Output_File_SN = open (str (Grand_Age_1) + "_SN.txt", "a")         # Save the calculation of mean and standard deviation in a table format
            Output_File_Stat = open (str (Grand_Age_1) + "_Stat.txt", "a")      # Save the calculation of mean, standard deviation and number of exact and approximate recovery in a table format
            df_SN_Sorted1 = pd.DataFrame (columns = None) ###
            df_Stat_Sorted = df_SN_Sorted.sort_values (by = [df.columns [2], df.columns [3]]) ### Sort clean data based on F(x), then based on S/N

            Grand_Age1_SN = '{0:.1f}'.format (float (str (Grand_Age_1)) * 0.1)
            Grand_Age2_SN = '{0:.1f}'.format (float (str (Grand_Age_2)) * 0.1)

            for f_x in range (0, 100, 10):
                for SN in range (50, 110, 10):

                    File_Name_SN = str (Grand_Age1_SN) + " " + str (Grand_Age2_SN) + " " + str (f_x) + " " + str (SN)
                    df_SN_Sorted1 = df_Stat_Sorted.loc [ (df_Stat_Sorted [2] == f_x) & (df_Stat_Sorted [3] == SN) ]

                    if f_x == 0:
                        diff_ages_0 = (df_SN_Sorted [1] - df_SN_Sorted [8]).round (1) # Special case when f_x = 0 ==> (output_Age1 - input_Age2)

                        df_age1 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_0 == -0.1) ]
                        df_age11 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_0 == 0.0) ]
                        df_age111 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_0 == 0.1) ]
                        df_age1111 = len (df_age1) + len (df_age11) + len (df_age111)

                        df_fx_Exact = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (df_SN_Sorted [10] == 100) ]

                        # Fill these columns with the same values for age1 since they are not applicable here (to mainain shape of the data file)
                        df_age22 = len (df_age11)
                        df_age2222 = len (df_age1) + len (df_age11) + len (df_age111)
                        df_fx_Approx = len (df_fx_Exact)

                        Output_File_Stat. write (File_Name_SN + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( )) + " " + '{0:.2f}'.format (df_SN_Sorted1 [8].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) + (df_SN_Sorted1 [8].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) - (df_SN_Sorted1 [8].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) - df_SN_Sorted1 [0].mean( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( )) + " " +  '{0:.2f}'.format (df_SN_Sorted1 [9].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) + (df_SN_Sorted1 [9].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) - (df_SN_Sorted1 [9].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) - df_SN_Sorted1 [1].mean ( )) + " " + '{0:.0f}'.format (df_SN_Sorted1 [10].mean ( )) + " " +  '{0:.0f}'.format (df_SN_Sorted1 [10].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) + (df_SN_Sorted1 [10].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) - (df_SN_Sorted1 [10].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) - df_SN_Sorted1 [2].mean ( )) + " " + str (len (df_age11)) + " " + str (df_age1111) + " " + str (df_age22) + " " + str (df_age2222) + " " + str (len (df_fx_Exact)) + " " + str (df_fx_Approx) + "\n") ###

                    else:
                        diff_ages_others_1 = (df_SN_Sorted [0] - df_SN_Sorted [8]).round (1)

                        diff_ages_others_2 = (df_SN_Sorted [1] - df_SN_Sorted [9]).round (1)

                        diff_ages_others_FX = (df_SN_Sorted [2] - df_SN_Sorted [10])

                        df_age1 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_1 == -0.1) ]
                        df_age11 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_1 == 0.0) ]
                        df_age111 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_1 == 0.1) ]
                        df_age1111 = len (df_age1) + len (df_age11) + len (df_age111)

                        df_age2 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_2 == -0.1) ]
                        df_age22 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_2 == 0.0) ]
                        df_age222 = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (diff_ages_others_2 == 0.1) ]
                        df_age2222 = len (df_age2) + len (df_age22) + len (df_age222)

                        df_fx_Exact = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & (df_SN_Sorted [2] == df_SN_Sorted [10]) ]
                        df_fx_Approx = df_SN_Sorted.loc [ (df_SN_Sorted [2] == f_x) & (df_SN_Sorted [3] == SN) & ((diff_ages_others_FX >= -5) & (diff_ages_others_FX <= 5)) ]

                        Output_File_Stat. write (File_Name_SN + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( )) + " " + '{0:.2f}'.format (df_SN_Sorted1 [8].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) + (df_SN_Sorted1 [8].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) - (df_SN_Sorted1 [8].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [8].mean ( ) - df_SN_Sorted1 [0].mean( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( )) + " " +  '{0:.2f}'.format (df_SN_Sorted1 [9].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) + (df_SN_Sorted1 [9].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) - (df_SN_Sorted1 [9].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [9].mean ( ) - df_SN_Sorted1 [1].mean ( )) + " " + '{0:.0f}'.format (df_SN_Sorted1 [10].mean ( )) + " " +  '{0:.0f}'.format (df_SN_Sorted1 [10].std ( )) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) + (df_SN_Sorted1 [10].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) - (df_SN_Sorted1 [10].std ( ))) + " " + '{0:.1f}'.format (df_SN_Sorted1 [10].mean ( ) - df_SN_Sorted1 [2].mean ( )) + " " + str (len (df_age11)) + " " + str (df_age1111) + " " + str (len (df_age22)) + " " + str (df_age2222) + " " + str (len (df_fx_Exact)) + " " + str (len (df_fx_Approx)) + "\n") ###
            Output_File_Stat.close ( )
# 68_Stat.txt ==> 6.8 7.0 0 50 7.0 0.05 7.0 6.9 0.2 7.6 1.10 8.7 6.5 0.6 53 288 1.7 25.0 53.3 18 30 18 30 0 0 -- 25 columns --
#              Age1 Age2 F(x) SN M(Out_Age1) STD(Out_Age1) M(Out_Age1)+STD(Out_Age1) M(Out_Age1)-STD(Out_Age1) M(Out_Age1)-M(Inp_Age1)
#                                M(Out_Age2) STD(Out_Age2) M(Out_Age2)+STD(Out_Age2) M(Out_Age2)-STD(Out_Age2) M(Out_Age2)-M(Inp_Age2)
#                                M(Out_FX) STD(Out_FX) M(Out_FX)+STD(Out_FX) M(Out_FX)-STD(Out_FX) M(Out_FX)-M(Inp_FX)
#                                Exact_Rec(Age1) Approx_Rec(Age1) Exact_Rec(Age2) Approx_Rec(Age2) Exact_Rec(FX) Approx_Rec(FX)

################################################################################
################################################################################

df_00_Stat = pd.DataFrame (columns = None)
df_10_Stat = pd.DataFrame (columns = None)
df_20_Stat = pd.DataFrame (columns = None)
df_30_Stat = pd.DataFrame (columns = None)
df_40_Stat = pd.DataFrame (columns = None)
df_50_Stat = pd.DataFrame (columns = None)
df_60_Stat = pd.DataFrame (columns = None)
df_70_Stat = pd.DataFrame (columns = None)
df_80_Stat = pd.DataFrame (columns = None)
df_90_Stat = pd.DataFrame (columns = None)

df_Grand_00_Stat = pd.DataFrame (columns = None)
df_Grand_10_Stat = pd.DataFrame (columns = None)
df_Grand_20_Stat = pd.DataFrame (columns = None)
df_Grand_30_Stat = pd.DataFrame (columns = None)
df_Grand_40_Stat = pd.DataFrame (columns = None)
df_Grand_50_Stat = pd.DataFrame (columns = None)
df_Grand_60_Stat = pd.DataFrame (columns = None)
df_Grand_70_Stat = pd.DataFrame (columns = None)
df_Grand_80_Stat = pd.DataFrame (columns = None)
df_Grand_90_Stat = pd.DataFrame (columns = None)

for root, dirs, files in os.walk ("."):
    for Grand_File_Stat in files:
        if "_Stat.txt" in Grand_File_Stat:

            df_Stat = pd.read_csv (Grand_File_Stat, engine = 'python', header = None, delim_whitespace = True)

            # Take the range of rows that is corresponding to each fraction value for each file
            df_00_Stat = df_Stat [0 : 6]
            df_10_Stat = df_Stat [6 : 12]
            df_20_Stat = df_Stat [12 : 18]
            df_30_Stat = df_Stat [18 : 24]
            df_40_Stat = df_Stat [24 : 30]
            df_50_Stat = df_Stat [30 : 36]
            df_60_Stat = df_Stat [36 : 42]
            df_70_Stat = df_Stat [42 : 48]
            df_80_Stat = df_Stat [48 : 54]
            df_90_Stat = df_Stat [54 : 61]

            # Collect all rows that is corresponding for each fraction value from all ages files into one dataframe (one age file)
            df_Grand_00_Stat = df_Grand_00_Stat.append (df_00_Stat, ignore_index = True)
            df_Grand_10_Stat = df_Grand_10_Stat.append (df_10_Stat, ignore_index = True)
            df_Grand_20_Stat = df_Grand_20_Stat.append (df_20_Stat, ignore_index = True)
            df_Grand_30_Stat = df_Grand_30_Stat.append (df_30_Stat, ignore_index = True)
            df_Grand_40_Stat = df_Grand_40_Stat.append (df_40_Stat, ignore_index = True)
            df_Grand_50_Stat = df_Grand_50_Stat.append (df_50_Stat, ignore_index = True)
            df_Grand_60_Stat = df_Grand_60_Stat.append (df_60_Stat, ignore_index = True)
            df_Grand_70_Stat = df_Grand_70_Stat.append (df_70_Stat, ignore_index = True)
            df_Grand_80_Stat = df_Grand_80_Stat.append (df_80_Stat, ignore_index = True)
            df_Grand_90_Stat = df_Grand_90_Stat.append (df_90_Stat, ignore_index = True)

# Sort the dataframes (tables) based on the fourth column (S/N), then based on the first column (real age)
df_Grand_00_Stat = df_Grand_00_Stat.sort_values (by = [df_Grand_00_Stat.columns [3], df_Grand_00_Stat.columns [0]])
df_Grand_10_Stat = df_Grand_10_Stat.sort_values (by = [df_Grand_10_Stat.columns [3], df_Grand_10_Stat.columns [0]])
df_Grand_20_Stat = df_Grand_20_Stat.sort_values (by = [df_Grand_20_Stat.columns [3], df_Grand_20_Stat.columns [0]])
df_Grand_30_Stat = df_Grand_30_Stat.sort_values (by = [df_Grand_30_Stat.columns [3], df_Grand_30_Stat.columns [0]])
df_Grand_40_Stat = df_Grand_40_Stat.sort_values (by = [df_Grand_40_Stat.columns [3], df_Grand_40_Stat.columns [0]])
df_Grand_50_Stat = df_Grand_50_Stat.sort_values (by = [df_Grand_50_Stat.columns [3], df_Grand_50_Stat.columns [0]])
df_Grand_60_Stat = df_Grand_60_Stat.sort_values (by = [df_Grand_60_Stat.columns [3], df_Grand_60_Stat.columns [0]])
df_Grand_70_Stat = df_Grand_70_Stat.sort_values (by = [df_Grand_70_Stat.columns [3], df_Grand_70_Stat.columns [0]])
df_Grand_80_Stat = df_Grand_80_Stat.sort_values (by = [df_Grand_80_Stat.columns [3], df_Grand_80_Stat.columns [0]])
df_Grand_90_Stat = df_Grand_90_Stat.sort_values (by = [df_Grand_90_Stat.columns [3], df_Grand_90_Stat.columns [0]])

# Save the output into 10 files to be used in Gnuplot to generate needed plots
# StepSize2_00_Stat.txt ==> 6.8 7.0 0 50 7.0 0.05 7.0 6.9 0.2 7.6 1.1 8.7 6.5 0.6 53 2881.7 25.0 53.3 18 30 18 30 0 0
df_Grand_00_Stat.to_csv ("StepSize2_00_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_10_Stat.to_csv ("StepSize2_10_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_20_Stat.to_csv ("StepSize2_20_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_30_Stat.to_csv ("StepSize2_30_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_40_Stat.to_csv ("StepSize2_40_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_50_Stat.to_csv ("StepSize2_50_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_60_Stat.to_csv ("StepSize2_60_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_70_Stat.to_csv ("StepSize2_70_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_80_Stat.to_csv ("StepSize2_80_Stat.txt", header = None, index = None, sep = " ", mode = "w")
df_Grand_90_Stat.to_csv ("StepSize2_90_Stat.txt", header = None, index = None, sep = " ", mode = "w")

################################################################################
######################## Add columns to clean data file ########################

for root, dirs, files in os.walk ("."):
    for StepSize2_Stat_Files in files:
        if "StepSize2_" in StepSize2_Stat_Files: # StepSize2_00_Stat.txt
            StepSize2_Stat_Name = StepSize2_Stat_Files.split (".") # StepSize2_00_Stat.txt
            Grand_Age1_StepSize2_Stat = StepSize2_Stat_Files [0] # StepSize2_00_Stat

            df_SN_Stat = pd.read_csv (StepSize2_Stat_Files, engine = 'python', header = None, delim_whitespace = True)

            B_Age1 = len (df_SN_Stat.columns)      # 26
            C_Age1 = len (df_SN_Stat.columns) + 1  # 27

            B_Age2 = len (df_SN_Stat.columns) + 2  # 28
            C_Age2 = len (df_SN_Stat.columns) + 3  # 29

            B_FX = len (df_SN_Stat.columns) + 4    # 30
            C_FX = len (df_SN_Stat.columns) + 5    # 31

            df_SN_Stat [B_Age1] = (df_SN_Stat [8] + df_SN_Stat [5]).round (2) # Add a new column at the end (A_Age1 + STD (age1))
            df_SN_Stat [C_Age1] = (df_SN_Stat [8] - df_SN_Stat [5]).round (2) # Add a new column at the end (A_Age1 - STD (age1))

            df_SN_Stat [B_Age2] = (df_SN_Stat [13] + df_SN_Stat [10]).round (2) # Add a new column at the end (A_Age2 + STD (age2))
            df_SN_Stat [C_Age2] = (df_SN_Stat [13] - df_SN_Stat [10]).round (2) # Add a new column at the end (A_Age2 - STD (age2))

            df_SN_Stat [B_FX] = (df_SN_Stat [18] + df_SN_Stat [15]).round (2) # Add a new column at the end (A_FX + STD (FX))
            df_SN_Stat [C_FX] = (df_SN_Stat [18] - df_SN_Stat [15]).round (2) # Add a new column at the end (A_FX - STD (FX))

            df_SN_Stat.to_csv (StepSize2_Stat_Files, sep = " ", header = None, index = None, mode = "w")
# 68_Stat.txt ==> 6.8 7.0 0 50 7.0 0.05 7.0 6.9 0.2 7.6 1.10 8.7 6.5 0.6 53 288 1.7 25.0 53.3 18 30 18 30 0 0 -- 25 columns --
# 1-Age1 2-Age2 3-F(x) 4-SN 5-M(Out_Age1) 6-STD(Out_Age1) 7-M(Out_Age1)+STD(Out_Age1) 8-M(Out_Age1)-STD(Out_Age1) 9-M(Out_Age1)-M(Inp_Age1)
# 10-M(Out_Age2) 11-STD(Out_Age2) 12-M(Out_Age2)+STD(Out_Age2) 13-M(Out_Age2)-STD(Out_Age2) 14-M(Out_Age2)-M(Inp_Age2)
# 15-M(Out_FX) 16-STD(Out_FX) 17-M(Out_FX)+STD(Out_FX) 18-M(Out_FX)-STD(Out_FX) 19-M(Out_FX)-M(Inp_FX)
# 20-Exact_Rec(Age1) 21-Approx_Rec(Age1) 22-Exact_Rec(Age2) 23-Approx_Rec(Age2) 24-Exact_Rec(FX) 25-Approx_Rec(FX)

################################################################################
################################################################################
