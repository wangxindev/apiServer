
def create_adset_name(serverData={}):
    if serverData['domain'] == 1:
        return True, 'adset_bg_name'
    elif serverData['domain'] == 2:
        return True, 'adset_ys_name'
    elif serverData['domain'] == 3:
        return True, 'adset_nc_name'
    else:
        return False, 'adset name err'