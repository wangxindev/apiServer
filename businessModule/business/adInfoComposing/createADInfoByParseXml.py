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
    if 'alias' in nodeChild.attrib.keys():
        aliasNode = AliasMgr().getAliasPoint(nodeChild.attrib['alias'])
        aliasNode.otherInfo = dataCenter.getMapData()
        aliasValue = aliasNode.value
        if aliasValue != None:
            adMapMgr.addAdInfo(aliasNode.name, aliasValue)
            return None

        tempMap = {}
        for key in aliasNode.strInfoClassObjList.keys():
            node = aliasNode.strInfoClassObjList[key]
            node.otherInfo = dataCenter.getMapData()
            tempValue = node.value
            if tempValue != None:
                tempMap[node.name] = node.value
        adMapMgr.addAdInfo(aliasNode.name, tempMap)

#生成对象树，并解析xml
def parseXmlAndGetAdInfo(sku, doman):
    parseXml()
    dataCenter = baseDataCenter({'key':sku,'doman':doman})
    adMap = ADMapMgr()
    for child in root:
        if child.tag == 'execute':
            for nodeChild in child:
                #print(nodeChild.attrib)
                parseNode(nodeChild, adMap, dataCenter)
    return adMap.getAdInfo()

print('='*30)
print(parseXmlAndGetAdInfo('sku88888888', '0'))
print('='*30)
