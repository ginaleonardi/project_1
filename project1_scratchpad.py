import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

census_csv = pd.read_csv('/Users/joshuafeinberg/Documents/U-of-O-Bootcamp/Bootcamp_Class_Folder/projects/PUFs/clean_master_merge.csv')


#dropping columns that don't have data for these columns
clean_census = census_csv.dropna(subset=['ANXIOUS', 'WORRY', 'INTEREST', 'DOWN'])


#dropping unnessary columns
clean_census = clean_census.drop(['RRACE.1','EEDUC.1'], axis=1)

# DROP RRACE.1, SCRAM, EEDUC.1
#renaming this column
clean_census = clean_census.rename(columns={'TENURE':'HOME OWNERSHIP',
                                            'EEDUC':'EDUCATION',
                                            'RRACE':'RACE',
                                            'TBIRTH_YEAR':'BIRTH YEAR',
                                            'RHISPANIC':'HISPANIC',
                                            'MS':'MARTIAL STATUS',
                                            'EGENID_BIRTH':'GEN ASN @ BIRTH',
                                            'GENID_DESCRIBE':'GEN ID DESCRIBE',
                                            'SEXUAL_ORIENTATION': 'SEXUAL ORIENTATION',
                                            'ANYWORK': 'EMPLOY STATUS 7D',
                                            'WEEK':'SERVEY DATE',
                                            'KIDS_LT5Y':'KIDS 0-5',
                                            'KIDS_5_11Y':'KIDS 5-11',
                                            'KIDS_12_17Y':'KIDS 12-17',
                                            'EST_ST':'STATE',
                                            'WEEK': 'WEEK'
                                            })
print(clean_census.head())

#select columns for analysis based on race   
