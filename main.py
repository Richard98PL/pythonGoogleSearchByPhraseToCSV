import requests
import json
import urllib.parse
  
f = open('accounts.json')
data = json.load(f)
f.close()  

resultDict = {}
k = 0
for i in data:
    if k < 400:
        URL = "http://google.com/search?q=" + urllib.parse.quote(str(i["Account"] + " webpage"))
        PARAMS = {}
        r = requests.get(url = URL, params = PARAMS)
        response = str(r.content)
        response = response.replace("www.google.com/", "")
        response = response.replace("!", "")
        f = open("result.html", "w")
        f.write(response)
        f.close()
        
        print(URL)
        lastAd = response.rfind("Reklama")
        if lastAd > 0 :
            response = response[lastAd:]
            lastAdWWW = response.find('www.')
            response = response[lastAdWWW+10:]

        firstWWW = response.find('www.')
        textNearFirstWWW = response[firstWWW:firstWWW+100]
        textNearFirstWWW = textNearFirstWWW.replace("<", "")
        print(str(i["Account"]))
        firstSlash = textNearFirstWWW.find('/')
        finalText = textNearFirstWWW[0:firstSlash]
        print(finalText)
        resultDict[str(i["Account"])] = finalText
    
        k = k + 1

        # if str(i["Account"]) == 'Advance B2B | Growth Marketing Agency':
        #     break

print (resultDict)
with open('results.csv', 'w') as f:
    for key in resultDict.keys():
        f.write("%s,%s"%('"' + key + '"','"' + resultDict[key] + '",\n'))


