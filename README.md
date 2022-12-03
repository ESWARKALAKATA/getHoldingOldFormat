# getHoldingOldFormat

Since Angle broking decommissioned the old platform there were a lot of bugs like 

Ex : when you download the holdings data you can see the error in data ( This will be address here)

The Holdings.py file will give you, current holding data from your portfolio with out any errors. 

Step1 :-  Create an app (API) -
  1. Login here - https://smartapi.angelbroking.com/apps
  2. Click on Create an App
  3. ![image](https://user-images.githubusercontent.com/53943052/205432249-959e5eb7-27f6-4bbc-95d9-a46abef5012e.png)
  4. Fill the details in above form, Redirect URL - u can give http://localhost:4505/
  
Step2 :- Need to enable Enable TOTP
  1. Login here with ur ClientID and angleOne Password - https://smartapi.angelbroking.com/enable-totp
  2. Here you will be presented with the QR code 
  3. Download Microsoft Authenticator application 
  4. Scan the (2) scan the QR from the Authenticator app 
  5. Now Topt is registered in  Microsoft Authenticator
  ( Note:- Every time when you run the getHoldingdata.py you need to provide this TOTP ) 
  
Sept3 :- 


  


