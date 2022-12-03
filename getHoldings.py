
# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)
import stockCred as cred

import pandas as pd
import datetime
 


#create object of call
obj = SmartConnect(api_key= cred.key
                #optional
                #access_token = 'd8400597-2597-4719-97ac-e361e1937a0b',
                #refresh_token = "your refresh_token")
)
data = obj.generateSession(cred.userName,cred.password, 535087)

cs = obj.holding()



df = pd.DataFrame(cs['data']) #saving this for later 


df1 = df[["tradingsymbol","averageprice","quantity","ltp"]] #filtering the required data

for i in cs['data']:
    
    lt = obj.ltpData(i['exchange'],i['tradingsymbol'],i['symboltoken']) # getting Ltp data from the api
    df1.loc[df1["tradingsymbol"] == lt['data']['tradingsymbol'], "ltp"] = lt['data']['ltp'] # adding Ltp values to daatframe 


# Using + operator to combine two columns
df1["Buy amount"] = df1['averageprice'] * df1["quantity"]

#Current Vlaue Calculation

df1["Current Value"] = df1['ltp'] * df1["quantity"]


#Gain or Loss Calculation

df1["GainOrLoss"] = df1['Current Value'] - df1["Buy amount"]



#current date is for printing file name 
current_date = str(datetime.datetime.now()).split()[0]


df1.to_csv(current_date + " Holdings", sep='\t')

  

