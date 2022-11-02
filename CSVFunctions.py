'''
Author: Brett Balquist
Date: 10/21/22
Last modified: 10/21/22
Purpose: Take research CSV files clean them up and then generate excel sheets for them
'''
import pandas as pd
def dari_convert(file_name):
    ##Reads the csv file and makes the dataframe
    df = pd.read_csv(file_name)
    return df
def remove_nans(file_name):
    ## reads for blank spaces and removes rows and columns with over majority blank
    df = dari_convert(file_name)
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    ## Drops rows and columns where over half of data is missing
    df.dropna(thresh = (cols/2), axis = 0, inplace = True)
    df.dropna(thresh= (rows/2),axis = 1, inplace = True)
    return df

def to_excel(file_name):
    ## converts the cleaned csv file to an excel sheet
    df = remove_nans(file_name)
    mystring = file_name.replace(".csv", "")
    ##create output excel file
    resultExcelFile = pd.ExcelWriter(f"{mystring}.xlsx")
    ##converting an output
    df.to_excel(resultExcelFile, index=False)
    ##save excel file
    resultExcelFile.save()


def main():
    usi = input("Enter name of CSV file (type 'stop' to stop): ")
    while usi.lower() != "stop":
        if usi[-4:] != ".csv":
            print("Invalid file name (make sure to include .csv)")
        else:
            remove_nans(usi)
            to_excel(usi)
        usi = input("Enter name of CSV file (type 'stop' to stop): ")

main()