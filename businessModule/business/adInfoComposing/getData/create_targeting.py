import requests
import json

def getBgData(sku):
    payload = {'com': 'product', 't': "interfToObtainProducts", 'zmkm': 1, 'sku': sku}
    try:
        r = requests.get("https://gbeta2.banggood.com/index.php", params=payload)
        return True, json.loads(r.text)
    except Exception:
        return False, '获取bg数据失败'

def getSemTargeting(domain, cat_id):
    payload = {'com': 'api', 't': "getTargetingByCat", 'domain': domain, 'cat_id': cat_id, 'token':'8e429c852f7e9646113aa9f270b6ad7f'}
    try:
        r = requests.get("https://sem.banggood.com/index.php", params=payload)
        return True, json.loads(r.text)
    except Exception:
        return False, '获取bg数据失败'

def saveData(data, serverData, key):
    if key in data:
        serverData[key] = data[key]
        return data[key]
    return None

def create_targeting(serverData={}):

    domain = None
    if 'domain' in serverData.keys():
        domain = serverData['domain']
    if domain is None:
        print(str(serverData))
        return False, 'get domain err'

    b = True
    Data = {}
    if domain == '1':
        b,Data =getBgData(serverData['key'])
    else:
        print('domain:' + str(domain))
        raise NameError

    if not b:
        print(str(serverData))
        return b, 'get web data error'

    Data = Data[0]
    saveData(Data,serverData,'product_id')
    cat_id = saveData(Data,serverData,'category_id')
    saveData(Data,serverData,'category_name')
    saveData(Data,serverData,'product_title')
    saveData(Data,serverData,'product_url')
    saveData(Data,serverData,'discount')
    saveData(Data,serverData,'product_attr')

    if cat_id is not None and domain is not None:
        cat_id = serverData['category_id'][(len(serverData['category_id'])-1)]
    else:
        print(str(serverData))
        return b, 'get web category_id or domain err'

    b, semData = getSemTargeting(domain, cat_id)

    if not b or semData['code'] is not 200:
        print(str(serverData))
        return b, 'get sem targeting err'

    print('target:' + str(semData))
    return b, semData['data']
