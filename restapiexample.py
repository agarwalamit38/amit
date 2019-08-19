
# REST API Call to Get Auth Key And Post Data

import requests

def getAuthKey(url) :

    response = requests.get(url)   # Making call to get authKey

    #Check for response code

    if( response.status_code == 201 ):
          jsonPayLoad = response.json()
          authKey = jsonPayLoad['key']   
          return authKey

    else:
         return None


        
def postData(url,authKey,dataPayLoad) :
     #Making a call to POST data 
     response = requests.post(url,json =dataPayLoad,headers={'Authorization':'bearer '+authKey}) 
     if ( response.status_code == 202) :
         return True
     else:
         return False   






url = "https://interns.bcgdvsydney.com/api/v1/key" 
authKey = getAuthKey(url)
dataPayLoad = {
                       "name":"Amit Agarwal",
                       "email":"agarwalamit38@gmail.com"
              }
url =url+"/submit"
status = postData(url,authKey,dataPayLoad)
if(status) :
 print("Sucess")
else :
 print("Failure")   







      
