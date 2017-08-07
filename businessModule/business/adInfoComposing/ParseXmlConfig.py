import sys
import logging
import xml.dom.minidom
from xml.etree import ElementTree as ET

loggerInfo = logging.getLogger("infoLogger")

def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

#别名管理器
#别名仅能指向一级的xml节点 module节点
@Singleton
class AliasMgr(object):
    def __init__(self):
        self._aliasList = {} #别名管理器，方便查找别名

    # strname 类属性名，xml属性中的name字段
    # point 对象的引用，xml中的一个节点
    def addAliasClass(self, strName, point):
        self._aliasList[strName] = point

    # strname 类属性名，xml属性中的name字段
    def getAliasPoint(self, strName):
        if strName in self._aliasList.keys():
            return self._aliasList[strName]

class AttBase(object):
    def __init__(self):
        self._name = None #信息名
        self._type = None #信息数据类型
        self._default = None #信息默认值
        self._enable = 'on' #此条信息是否启用
        self._getFunc = None #获取算法数据的头文件
        self._getImportPackageName = None #获取算法数据的包名
        self._alias = None #别名，可以指向module，用module代替此node
        self._value = None#最终的结果
        self._otherInfo = None

        self.mapInfo = {} #存放字典类型的数据
        self.aliasMgr = AliasMgr()

    @property
    def value(self):
        # 如果配置属性为off表示此节点不可用，直接返回None
        if self.enable == 'off':
            return None

        if self._value != None:
            return self._value

        #如果func 和 importPackageName 不为None 说明通过此方法获取属性值
        if self.func != None:
            if self.importPackageName != None:
                exec("import " + str(self.importPackageName))
                exec("self._value = " + str(self.importPackageName) + "." + str(self.func) + "(self.otherInfo)")

        if self._value==None and self.default!=None:
            self._value = self.default

        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name=None):
        if name != None:
            self._name = name
            self.mapInfo['name'] = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type=None):
        if type != None:
            self._type = type
            self.mapInfo['type'] = type

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, default=None):
        if default != None:
            if self.type == 'int':
                default = int(default)
            elif self.type == 'float':
                default = float(default)
            elif self.type == 'tuple':
                default = tuple(default)
            elif self.type == 'array':
                default = eval(default)
            elif self.type == 'object':
                default = eval(default)
            else:
                default = str(default)
            self._default = default
            self.mapInfo['default'] = default

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable='on'):
        self._enable = enable
        self.mapInfo['enable'] = enable

    @property
    def func(self):
        return self._getFunc

    @func.setter
    def func(self, Func=None):
        if Func != None:
            self._getFunc =  Func
            self.mapInfo['func'] = Func

    @property
    def importPackageName(self):
        return self._getImportPackageName

    @importPackageName.setter
    def importPackageName(self, ImportPackageName=None):
        if ImportPackageName != None:
            self._getImportPackageName = ImportPackageName
            self.mapInfo['importPackageName'] = ImportPackageName

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, alias=None):
            self._alias = alias
            self.mapInfo['alias'] = alias
    @property
    def otherInfo(self):
        return self._otherInfo

    @otherInfo.setter
    def otherInfo(self, info):
        self._otherInfo = info


    def initByMap(self, infoMap):
        for key in infoMap.keys():
            if 'name' == key:
                #self.getNameAtt(infoMap['name'])
                self.name = infoMap['name']
            elif 'type' == key:
                self.type = infoMap['type']
            elif 'default' == key:
                if self.type == None and 'type' in infoMap.keys():
                    self.type = infoMap['type']
                self.default = infoMap['default']
            elif 'enable' == key:
                self.enable = infoMap['enable']
            elif 'func' == key:
                self.func = infoMap['func']
            elif 'importPackageName' == key:
                self.importPackageName = infoMap['importPackageName']
            elif 'alias' == key:
                self.alias = infoMap['alias'] #在module模块中，无效
            # else:
            #     loggerInfo("属性中不存在的字段:(%s,%s)"%(key,str(infoMap[key])))

class NodeBase(AttBase):
    def __init__(self):
        super(NodeBase, self).__init__()

class ModuleBase(NodeBase):
    def __init__(self):
        super(NodeBase, self).__init__()
        self.__strInfoClassList = {}#信息类的集合
        self.moduleMapInfo = {}

    @property
    def strInfoClassObjList(self):
        return self.__strInfoClassList

    @strInfoClassObjList.setter
    def strInfoClassObjList(self, strInfoObj):
        self.__strInfoClassList[strInfoObj.name] = strInfoObj
        self.moduleMapInfo[strInfoObj.name] = strInfoObj.mapInfo

@Singleton
class ModuleBaseMgr(object):
    def __init__(self):
        self.moduleListMapInfo = {}
        self.__moduleList = {}

    def addModuleClassObject(self, moduleObj):
        self.__moduleList[moduleObj.name] = moduleObj
        self.moduleListMapInfo[moduleObj.name] = moduleObj.moduleMapInfo
        moduleObj.aliasMgr.addAliasClass(moduleObj.name, moduleObj)


class ADMapMgr(object):
    def __init__(self):
        self.__adMap = {}

    def addAdInfo(self,name,data):
        if name in self.__adMap.keys():
            if not isinstance(self.__adMap[name], list):
                temp = self.__adMap[name]
                self.__adMap[name] = []
                self.__adMap[name].append(temp)
                self.__adMap[name].append(data)
            else:
                self.__adMap[name].append(data)
        else:
            self.__adMap[name] = data

    def getAdInfo(self):
        return self.__adMap


moduleMgr =  ModuleBaseMgr()
#打开xml文档
#configPath = '/Volumes/work/3.code/APIServer/businessModule/business/adInfoComposing/config/adconfig.xml'
configPath = sys.path[0] + str('/businessModule/business/adInfoComposing/config/adconfig.xml')
per=ET.parse(configPath)
root = per.getroot()

#生成对象树，并解析xml
def parseXml():
    print(root.tag)
    for child in root:
        #这一部分是生成对象树
        if child.tag == 'module':
            module = ModuleBase()
            module.initByMap(child.attrib)
            if 'array' in child.attrib.keys():
                module.array = child.attrib['array']
            moduleMgr.addModuleClassObject(module)
            for nodeChild in child:
                node = NodeBase()
                node.initByMap(nodeChild.attrib)
                module.strInfoClassObjList = node

#parseXml()
# print(moduleMgr.moduleListMapInfo)