import requests
import json

def getAdCreative(sku, domain):
    # http://169.46.64.183:3330/getAdText/?sku=SKU292714&doman=1
    payload = {'doman': domain, 'sku': sku}
    try:
        r = requests.get("http://169.46.64.183:3330/getAdText/", params=payload)
        return True, json.loads(r.text)
    except Exception:
        return False, '获取ad creative数据失败'

def create_creative(serverData={}):
    domain = None
    sku = None
    if 'domain' in serverData.keys():
        domain = serverData['domain']
    if 'key' in serverData.keys():
        sku = serverData['key']
    if sku is None:
        print(str(serverData))
        return False, 'get sku err'
    if domain is None:
        print(str(serverData))
        return False, 'get domain err'

    b = True
    b, Data = getAdCreative(sku=sku, domain=domain)

    if not b:
        return b, Data

    if "Succeed" in Data.keys():
        if Data['Succeed'] == True:
            Data = Data['data']
            if 'product_url' in serverData.keys():
                Data['product_url'] = serverData['product_url']
            else:
                return False, 'not product_url'
        elif "Message" in Data.keys():
            return False, Data['Message']
        else :
            return False, 'get ad creative err'
    else:
        return False, 'get ad creative err'

    return b,Data