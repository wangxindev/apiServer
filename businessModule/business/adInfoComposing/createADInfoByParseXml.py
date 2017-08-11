import sys
import types
import logging
import xml.dom.minidom
from xml.etree import ElementTree as ET


from  businessModule.business.adInfoComposing.ParseXmlConfig import AliasMgr, ADMapMgr, parseXml

class baseDataCenter(object):

    def __init__(self, mapData={}):
        self.mapData = mapData

    def setMapData(self, mapData):
        if mapData is not None:
            if types(mapData) is types.MappingProxyType:
               self.mapData = mapData

    def getMapData(self):
        if self.mapData is not None:
            return self.mapData
        return None

configPath = sys.path[0] + str('/businessModule/business/adInfoComposing/config/adInfo.xml')
per=ET.parse(configPath)
root = per.getroot()

#递归处理xml节点执行
def parseNode(nodeChild, adMapMgr, dataCenter):
    b = True
    if 'alias' in nodeChild.attrib.keys():
        aliasNode = AliasMgr().getAliasPoint(nodeChild.attrib['alias'])
        aliasNode.otherInfo = dataCenter.getMapData()

        tempMap = {}
        b, aliasValue = aliasNode.value
        if not b:
            return b, aliasValue

        if aliasValue != None:
            # adMapMgr.addAdInfo(aliasNode.name, {aliasNode.name:aliasValue})
            tempMap[aliasNode.name] = aliasValue

        for key in aliasNode.strInfoClassObjList.keys():
            node = aliasNode.strInfoClassObjList[key]
            node.otherInfo = dataCenter.getMapData()
            b, tempValue = node.value
            if not b:
                return b, tempValue
            if tempValue != None:
                tempMap[node.name] = node.value
        adMapMgr.addAdInfo(aliasNode.name, tempMap)

    return b,'ok'

#生成对象树，并解析xml
def parseXmlAndGetAdInfo(sku, domain, userData={}):
    parseXml()
    b = True
    dataCenter = baseDataCenter({'key':sku,'domain':domain, 'userData':userData})
    adMap = ADMapMgr()
    for child in root:
        if child.tag == 'execute':
            for nodeChild in child:
                print(nodeChild.attrib)
                b, error = parseNode(nodeChild, adMap, dataCenter)
    if b:
        return b, adMap.getAdInfo()
    else:
        return b , error

# print('='*30)
# print(parseXmlAndGetAdInfo('sku88888888', '0',{}))
# print('='*30)
