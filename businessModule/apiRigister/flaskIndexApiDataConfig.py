
desc = \
{
	"siteflag":0,
	"sku":"SKU623093",
	"product_id":"996086",
	"cat_path":"892,1985,5146,5150",
	"title":"5Pcs Multipurpose Blackhead Acne Comedone Extractor Remover Stainless Steel Tool Set Kit",
	"description":"Material: Stainless Steel Tools Color: Silver Case Color: Black Weight: App 89g Size: As seen from the pictures",
	"language":"en",
	"urlCallback":"处理完业务后调用的回调url，可以自己随意填，通过自己制定url的方式给自己传递某些信息等，例如获取这是哪一个广告的处理返回数据"
}

notes = {
    'googleTitleptimize': '<谷歌广告优化接口>事例：（引号需要改成双引号）' + str(desc),
    'getAdText': '<获取广告文本接口>get请求参数（暂时不支持post）：?sku=skuxxx&doman=1',
    'test': 'test',
	'adComposingApi':'广告组装api'
}

from app.app import getAppMgr

getAppMgr().insert('desc', desc)
getAppMgr().insert('notes', notes)
