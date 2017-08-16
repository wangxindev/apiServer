# {'userData': {'userData': 'hello'}, 'product_id': 1039040, 'category_name': ['Clothing and Apparel', "Women's Clothing", 'Plus Size'], 'domain': '1', 'key': 'SKU371288', 'product_attr': [{'name': 'color', 'value_name': ['Black', 'Green', 'Beige'], 'count': 3}, {'name': 'size', 'value_name': ['M', 'L', 'XL', '2XL'], 'count': 4}], 'discount': 0, 'product_url': 'https://gbeta2.banggood.com/Loose-Women-Lace-Crochet-Patchwork-Flare-Sleeve-Irregular-T-shirt-p-1039040.html', 'product_title': 'Loose Women Lace Crochet Patchwork Flare Sleeve Irregular T-shirt', 'category_id': [274, 278, 3103]}
# {
#     'userData': {
#         'userData': 'hello'
#     },
#     'product_id': 1039040,
#     'category_name': [
#         'ClothingandApparel',
#         "Women's Clothing",
#         'PlusSize'
#     ],
#     'domain': '1',
#     'key': 'SKU371288',
#     'product_attr': [
#         {
#             'name': 'color',
#             'value_name': [
#                 'Black',
#                 'Green',
#                 'Beige'
#             ],
#             'count': 3
#         },
#         {
#             'name': 'size',
#             'value_name': [
#                 'M',
#                 'L',
#                 'XL',
#                 '2XL'
#             ],
#             'count': 4
#         }
#     ],
#     'discount': 0,
#     'product_url': 'https: //gbeta2.banggood.com/Loose-Women-Lace-Crochet-Patchwork-Flare-Sleeve-Irregular-T-shirt-p-1039040.html',
#     'product_title': 'LooseWomenLaceCrochetPatchworkFlareSleeveIrregularT-shirt',
#     'category_id': [
#         274,
#         278,
#         3103
#     ]
# }
def create_ad_name(serverData={}):
    print('serverData:' + str(serverData))
    if serverData['domain'] == 1:
        return True, 'ad_bg_name'
    elif serverData['domain'] == 2:
        return True, 'ad_ys_name'
    elif serverData['domain'] == 3:
        return True, 'ad_nc_name'
    else:
        return False, 'ad name err'


