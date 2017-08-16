
import time

class AdObj(object):
    def init(self, data):
        self.data = data

    def assemble(self):
        return self.data

    def show(self):
        print(self.data)

class OtherInfo(AdObj):
    pass

class Campaign(AdObj):
    pass
    '''
    {'objective': (True, 'CONVERSIONS'), 'status': (True, 'PAUSED'), 'account_id': (True, '未定'),
     'dc_id': (True, '未定'), 'campaign_name': (True, 'campaign_name')}
    '''


class AdSet(AdObj):
    pass
    '''
    {
    'daily_budget': (True, 30), 
    'promoted_object': (True, {'custom_event_type': 'PURCHASE'}),
    'attribution_window_days': (True, 7), 
    'adsetName': (True, 'adsetName'), 'billing_event': (True, 'IMPRESSIONS'),
    'is_autobid': (True, 1), 
    'status': (True, 'ACTIVE'),
    'optimization_goal': (True, 'OFFSITE_CONVERSIONS'),
    'attribution_spec': (True, [{'window_days': 7, ' event_type': 'CLICK_THROUGH'}])}
    '''

class Targeting(AdObj):
    '''
    {'targeting': [{'interest_tag': 'clo', 'age_max': '64', 'age_min': '35',
                    'facebook_positions': ['feed', 'right_hand_column', 'instant_article'],
                    'geo_locations': {'regions': [], 'country_groups': ['europe'], 'countries': []},
                    'publisher_platforms': ['facebook', 'instagram', 'audience_network'], 'flexible_spec': [{
                                                                                                                'interests': [
                                                                                                                    {
                                                                                                                        'name': 'Coat (clothing)',
                                                                                                                        'id': '6003397760241'},
                                                                                                                    {
                                                                                                                        'name': 'Jacket',
                                                                                                                        'id': '6003281049823'},
                                                                                                                    {
                                                                                                                        'name': 'Blouse',
                                                                                                                        'id': '6002998047244'},
                                                                                                                    {
                                                                                                                        'name': 'Top (clothing)',
                                                                                                                        'id': '6003242238524'},
                                                                                                                    {
                                                                                                                        'name': 'Dresses',
                                                                                                                        'id': '6003188355978'},
                                                                                                                    {
                                                                                                                        'name': 'maxi dresses',
                                                                                                                        'id': '6003271346180'}]}],
                    'device_platforms': ['mobile', 'desktop'], 'instagram_positions': ['stream'], 'genders': [2]},
                   {'interest_tag': 'clo', 'age_max': '64', 'age_min': '35',
                    'facebook_positions': ['feed', 'right_hand_column', 'instant_article'],
                    'geo_locations': {'regions': [], 'country_groups': ['apec'], 'countries': []},
                    'publisher_platforms': ['facebook', 'instagram', 'audience_network'], 'flexible_spec': [{
                                                                                                                'interests': [
                                                                                                                    {
                                                                                                                        'name': 'Coat (clothing)',
                                                                                                                        'id': '6003397760241'},
                                                                                                                    {
                                                                                                                        'name': 'Jacket',
                                                                                                                        'id': '6003281049823'},
                                                                                                                    {
                                                                                                                        'name': 'Blouse',
                                                                                                                        'id': '6002998047244'},
                                                                                                                    {
                                                                                                                        'name': 'Top (clothing)',
                                                                                                                        'id': '6003242238524'},
                                                                                                                    {
                                                                                                                        'name': 'Dresses',
                                                                                                                        'id': '6003188355978'},
                                                                                                                    {
                                                                                                                        'name': 'maxi dresses',
                                                                                                                        'id': '6003271346180'}]}],
                    'device_platforms': ['mobile', 'desktop'], 'instagram_positions': ['stream'], 'genders': [2]},
                   {'interest_tag': 'web', 'age_max': '64', 'age_min': '35',
                    'facebook_positions': ['feed', 'right_hand_column', 'instant_article'],
                    'geo_locations': {'regions': [], 'country_groups': ['europe'], 'countries': []},
                    'publisher_platforms': ['facebook', 'instagram', 'audience_network'], 'flexible_spec': [{
                                                                                                                'interests': [
                                                                                                                    {
                                                                                                                        'name': 'Amazon.com',
                                                                                                                        'id': '6003002193982'},
                                                                                                                    {
                                                                                                                        'name': 'EBay',
                                                                                                                        'id': '6003319307848'},
                                                                                                                    {
                                                                                                                        'name': 'eBay Global',
                                                                                                                        'id': '6011406542962'},
                                                                                                                    {
                                                                                                                        'name': 'eBay  Fashion',
                                                                                                                        'id': '6011604327964'},
                                                                                                                    {
                                                                                                                        'name': 'Alibaba.com',
                                                                                                                        'id': '6003257148486'}]}],
                    'device_platforms': ['mobile', 'desktop'], 'instagram_positions': ['stream'], 'genders': [2]},
                   {'interest_tag': 'web', 'age_max': '64', 'age_min': '35',
                    'facebook_positions': ['feed', 'right_hand_column', 'instant_article'],
                    'geo_locations': {'regions': [], 'country_groups': ['apec'], 'countries': []},
                    'publisher_platforms': ['facebook', 'instagram', 'audience_network'], 'flexible_spec': [{
                                                                                                                'interests': [
                                                                                                                    {
                                                                                                                        'name': 'Amazon.com',
                                                                                                                        'id': '6003002193982'},
                                                                                                                    {
                                                                                                                        'name': 'EBay',
                                                                                                                        'id': '6003319307848'},
                                                                                                                    {
                                                                                                                        'name': 'eBay Global',
                                                                                                                        'id': '6011406542962'},
                                                                                                                    {
                                                                                                                        'name': 'eBay  Fashion',
                                                                                                                        'id': '6011604327964'},
                                                                                                                    {
                                                                                                                        'name': 'Alibaba.com',
                                                                                                                        'id': '6003257148486'}]}],
                    'device_platforms': ['mobile', 'desktop'], 'instagram_positions': ['stream'], 'genders': [2]}]}
    '''
    def assemble(self):
        return self.data['targeting']

class Ad(AdObj):
    '''
    {'slideshow_duration': (True, 1), 'call_to_action_type': (True, 'shop now'), 'display_link': (True, ''),
     'optimization_goal': (True, 'OFFSITE_CONVERSIONS'), 'see_more_link': (True, 'learn_more'),
     'adName': (True, 'adName'), 'slideshow_aspect_radio': (True, 'original'), 'type': (True, 'slideshow'),
     'slideshow_transition': (True, 'none')}
    '''
    pass

class Creative(AdObj):
    '''
    {'creative': {
        'product_url': 'https://gbeta2.banggood.com/Loose-Women-Lace-Crochet-Patchwork-Flare-Sleeve-Irregular-T-shirt-p-1039040.html',
        'description': 'Shop at banggood ', 'text': 'Low to US$15.81, Now or Next Year ! Hurry to pick yours ! ',
        'headline': 'Special Offer ! Take Chance ', 'urls': [
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/32c830c7-2f15-4b2c-87cd-49d643fead80.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/0a0de6b7-2858-4b4b-b935-5c8014ef2ec7.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/cac16eec-5ec9-45f5-829f-520f27f82d73.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/cbb19839-f828-4ce7-931e-4606205257e6.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/c2adc85d-5204-4d5b-b1ef-760ba41aa7aa.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/A1/53/6436e1de-c3e4-4b68-8976-81fdd5481ed7.jpg',
            'https://img2.banggood.com/thumb/large/oaupload/banggood/images/81/8D/cc209059-7abd-48b3-8ed3-c58e2b47547f.jpg']}}
    '''
    def assemble(self):
        self.data['creative']['see_more_link'] = self.data['creative']['product_url']
        self.data['creative']['product_url'] = None
        # print("create:" + str([self.data['creative']]))
        return [self.data['creative']]
        # return [self.data['creative']['creative']]

class Name(AdObj):

    def __init__(self):
        self.__operator='' #操作人
        self.__categoryCode ='' #类别代码
        self.__Level_3_classification_code = '' #3级分类代码
        self.__sku = '' #sku
        self.__date = '' #日期
        self.__price = '' #最终售价
        self.__Audience_positioning = '' #受众定位
        self.__countries = '' #国家
        self.__Audience_positioning_named = '' #受众定位命名
        self.__Put_position = '' #投放位置
        self.__set_date = '' #建立日期
        self.__Advertising = ''#广告形式

        self.__countries_key_value = {
            'south_america':'soa',
            'north_america': 'noa',
            'central_america': 'cea',
            'nafta': 'nafta',
            'eea': 'eea',
            'afta':'afta',
            'cisfta': 'cisfta',
            'mercosur': 'mer',
            'android_free_store': 'afsc',
            'android_paid_store': 'apsc',
            'itunes_app_store': 'itune',
            'apec': 'apec',
            'europe': 'euro',
        }

    #Campaign name：操作人-类别代码-三级分类代码-sku-日期-价格
    def getCompaignName(self, adInfo):
        self.__operator = 'ai'
        self.__categoryCode = '接口获取'
        self.__Level_3_classification_code = '接口获取'
        self.__sku = adInfo['key'][3:]
        self.__date = time.strftime('%m%d', time.localtime(time.time()))
        self.__price = '需要接口支持'

        return self.__operator + "-" + self.__categoryCode + "-" + self.__Level_3_classification_code \
            + "-" + self.__sku + "-" + self.__date + "-$" + self.__price


    #adset name：受众定位 + 类别代码 - sku - 国家 - 受众定位命名 - 投放位置 - 建立日期
    def getAdSetName(self,adset_targeting):
        #
        # {'flexible_spec': [{'interests': [{'id': '6003002193982', 'name': 'Amazon.com'},
        #                                   {'id': '6003319307848', 'name': 'EBay'},
        #                                   {'id': '6011406542962', 'name': 'eBay Global'},
        #                                   {'id': '6011604327964', 'name': 'eBay  Fashion'},
        #                                   {'id': '6003257148486', 'name': 'Alibaba.com'}]}],
        #  'genders': [2],
        #  'facebook_positions': ['feed', 'right_hand_column', 'instant_article'], 'age_min': '35', 'interest_tag': 'web',
        #  'publisher_platforms': ['facebook', 'instagram', 'audience_network'],
        #  'device_platforms': ['mobile', 'desktop'],
        #  'geo_locations': {'countries': [], 'country_groups': ['apec'], 'regions': []},
        #  'instagram_positions': ['stream'], 'age_max': '64'}

        self.__Audience_positioning = 'i'
        country_groups = adset_targeting['geo_locations']['country_groups']
        countries = adset_targeting['geo_locations']['countries']
        self.__countries = ''
        if country_groups != []:
            for country in country_groups:
                try:
                    self.__countries += self.__countries_key_value[country]
                except:
                    NameError("国家映射不存在")
        elif countries != []:
            for countrie in countries:
                self.__countries += countrie
        else:
            raise NameError("国家不存在")

        self.__Audience_positioning_named = adset_targeting['interest_tag']
        self.__Put_position = 'auto'
        self.__set_date = self.__date
        return  self.__Audience_positioning + self.__categoryCode \
            + "-" + self.__sku + "-" + self.__countries + "-" + self.__Audience_positioning_named \
            + "-" + self.__Put_position + "-" + self.__set_date


    #ad name：ad set name - 投放广告形式（其中需去除adset name内的日期）
    def getAdName(self, ad_info):
        self.__Advertising = ad_info['type']
        return self.__Audience_positioning + self.__categoryCode \
               + "-" + self.__sku + "-" + self.__countries + "-" + self.__Audience_positioning_named \
               + "-" + self.__Put_position + "-" + self.__Advertising



class AdvertisingRelease(object):
    def __init__(self):
        print("__init__ start")
        self.__campaign = Campaign()
        self.__adSet = AdSet()
        self.__targeting = Targeting()
        self.__ad = Ad()
        self.__creative = Creative()
        self.__name = Name()
        self.__otherInfo = OtherInfo()
        print("__init__ end")


    def getAdInfo(self, adInfo):
        print("get ad info start")
        self.__campaign.init(adInfo['campaign'])
        self.__adSet.init(adInfo['adset'])
        self.__targeting.init(adInfo['targeting'])
        self.__ad.init(adInfo['ad'])
        self.__creative.init(adInfo['creative'])
        self.__name.init(adInfo['name'])
        print("other start")
        self.__otherInfo.init(adInfo['otherInfo'])
        print("other end")

        self.assembleAd()
        print("get ad info end")

    def assembleAd(self):

        assemble_ad = self.__campaign.assemble()
        assemble_ad['campaign_name'] = self.__name.getCompaignName(self.__otherInfo.assemble())
        assemble_ad['adset'] = []
        adset_adset = self.__adSet.assemble()
        adset_Targeting_array = self.__targeting.assemble()
        for adset_targeting in adset_Targeting_array:
            adset_iter = adset_adset
            assemble_ad['adset'].append(adset_iter)
            adset_iter["targeting"] = adset_targeting
            adset_iter['name'] = self.__name.getAdSetName(adset_targeting)
            adset_iter['ads']=[]
            creative_array = self.__creative.assemble()
            creative_image_link_array = []
            for creative in creative_array:
                ad_tmp = {}
                adset_iter['ads'].append(ad_tmp)
                ad_tmp['creative'] = creative
                ad = self.__ad.assemble()
                ad_tmp['creative']['call_to_action_type'] = ad['call_to_action_type']
                ad_tmp['creative']['display_link'] = ad['display_link']
                ad_tmp['creative']['slideshow_aspect_radio'] = ad['slideshow_aspect_radio']
                ad_tmp['creative']['slideshow_duration'] = ad['slideshow_duration']
                ad_tmp['creative']['slideshow_transition'] = ad['slideshow_transition']
                creative_image_link_array.append(creative['see_more_link'])
                ad_tmp['ad_name'] = self.__name.getAdName(ad)
                ad_tmp['status'] = ad['status']

        print(self.sendAd(assemble_ad))

    def sendAd(self, ad):
        return True, '广告发布'+str(ad)
        # payload = {'doman': domain, 'sku': sku}
        # try:
        #     r = requests.get("http://169.46.64.183:3330/getAdText/", params=payload)
        #     return True, json.loads(r.text)
        # except Exception:
        #     return False, '获取ad creative数据失败'





'''
    {
        "account_id": "1282689771807379",
        "status": "PAUSED",
        "dc_id": "1000547",
        "campaign_name": "ld-fashion3-ht-house-SKU709351-0725-$14.59",
        "adset": [
            {
                "optimization_goal": "OFFSITE_CONVERSIONS",
                "billing_event": "IMPRESSIONS",
                "promoted_object": {
                    "custom_event_type": "PURCHASE"
                },
                "daily_budget": 30,
                "is_autobid": 1,
                "attribution_window_days": 7,
                "status": "ACTIVE",
                "attribution_spec": [
                    {
                        " event_type": "CLICK_THROUGH",
                        "window_days": 7
                    }
                ],
                "targeting": {
                    "geo_locations": {
                        "countries": [
                            "US"
                        ],
                        "country_groups": [],
                        "regions": []
                    },
                    "age_min": 18,
                    "flexible_spec": [],
                    "interest_tag": "amaz",
                    "publisher_platforms": [
                        "facebook",
                        "instagram",
                        "audience_network"
                    ],
                    "facebook_positions": [
                        "feed",
                        "right_hand_column",
                        "instant_article"
                    ],
                    "instagram_positions": [
                        "stream"
                    ],
                    "device_platforms": [
                        "mobile",
                        "desktop"
                    ]
                },
                "name": "ht-709351-US-amaz-auto-0725",
                "ads": [
                    {
                        "status": "ACTIVE",
                        "ad_name": "ht-709351-US-amaz-auto-s1",
                        "creative": {
                            "type": "slideshow",
                            "images": [
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/98/73/2df85ebb-0dd6-4c26-a48b-bd30c06d60ad.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/C7/F7/3a4b9f5d-8025-4fab-a089-4a6ad238ee4b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/83/54/c93f1bb7-5c03-4eae-9b1d-2412b1260e41.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/16/45/4b8ec862-7646-421a-83ab-099cb6278f6b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/B3/F8/5727fd6d-342c-4b54-a6a7-93eed6f6371b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/4B/4C/a448d7e1-1ab0-4df5-8d90-d1ae58c2844b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/9A/19/83128ee9-3247-4905-8bd0-97870860c42e.jpg"
                            ],
                            "image_headline": [
                                ""
                            ],
                            "image_link": [
                                "https://www.newchic.com/storage-boxes-4913/p-1173680.html"
                            ],
                            "image_desc": [
                                ""
                            ],
                            "text": "",
                            "see_more_link": "https://www.newchic.com/storage-boxes-4913/p-1173680.html",
                            "call_to_action_type": "learn_more",
                            "display_link": "",
                            "slideshow_aspect_radio": "original",
                            "slideshow_duration": 1000,
                            "slideshow_transition": "none"
                        }
                    }
                ]
            },
            {
                "optimization_goal": "OFFSITE_CONVERSIONS",
                "billing_event": "IMPRESSIONS",
                "promoted_object": {
                    "custom_event_type": "PURCHASE"
                },
                "daily_budget": 30,
                "is_autobid": 1,
                "attribution_window_days": 7,
                "status": "ACTIVE",
                "attribution_spec": [
                    {
                        " event_type": "CLICK_THROUGH",
                        "window_days": 7
                    }
                ],
                "targeting": {
                    "geo_locations": {
                        "countries": [],
                        "country_groups": [
                            "eea"
                        ],
                        "regions": []
                    },
                    "age_min": 65,
                    "flexible_spec": [],
                    "interest_tag": "amaz",
                    "publisher_platforms": [
                        "facebook",
                        "instagram",
                        "audience_network"
                    ],
                    "facebook_positions": [
                        "feed",
                        "right_hand_column",
                        "instant_article"
                    ],
                    "instagram_positions": [
                        "stream"
                    ],
                    "device_platforms": [
                        "mobile",
                        "desktop"
                    ]
                },
                "name": "ht-709351-eea-amaz-auto-0725",
                "ads": [
                    {
                        "status": "ACTIVE",
                        "ad_name": "ht-709351-eea-amaz-auto-s1",
                        "creative": {
                            "type": "slideshow",
                            "images": [
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/98/73/2df85ebb-0dd6-4c26-a48b-bd30c06d60ad.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/C7/F7/3a4b9f5d-8025-4fab-a089-4a6ad238ee4b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/83/54/c93f1bb7-5c03-4eae-9b1d-2412b1260e41.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/16/45/4b8ec862-7646-421a-83ab-099cb6278f6b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/B3/F8/5727fd6d-342c-4b54-a6a7-93eed6f6371b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/4B/4C/a448d7e1-1ab0-4df5-8d90-d1ae58c2844b.jpg",
                                "https://img2.newchic.com/thumb/large/oaupload/newchic/images/9A/19/83128ee9-3247-4905-8bd0-97870860c42e.jpg"
                            ],
                            "image_headline": [
                                ""
                            ],
                            "image_link": [
                                "https://www.newchic.com/storage-boxes-4913/p-1173680.html"
                            ],
                            "image_desc": [
                                ""
                            ],
                            "text": "",
                            "see_more_link": "https://www.newchic.com/storage-boxes-4913/p-1173680.html",
                            "call_to_action_type": "learn_more",
                            "display_link": "",
                            "slideshow_aspect_radio": "original",
                            "slideshow_duration": 1000,
                            "slideshow_transition": "none"
                        }
                    }
                ]
            }
        ],
        "objective": "CONVERSIONS"
    }
    '''
