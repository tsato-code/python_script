import numpy as np


def latlon_to_yx(latlon):
    # 東京駅を原点に
    c_lat, c_lon =  35.681194, 139.767056
    kyoku_hankei =  6356752.314
    sekido_hankei = 6378137
    tokyo_hankei = sekido_hankei * np.cos(c_lat * np.pi / 180.0)

    lat = latlon[0]
    lon = latlon[1]

    lon1_to_m = tokyo_hankei * np.pi /180.
    lat1_to_m = kyoku_hankei * np.pi /180.
    dy = (lat - c_lat) * lat1_to_m
    dx = (lon - c_lon) * lon1_to_m
    return [dy, dx]

east = [35.69784903, 139.5914377]
west = [35.70566008, 139.568008]

print(latlon_to_yx(east))
print(latlon_to_yx(west))
print(np.linalg.norm(np.array(latlon_to_yx(east)) - np.array(latlon_to_yx(west))))


"""
$ python test_latlon2yx.py
[1847.8132489336683, -15879.765169624843]
[2714.4200144623173, -17998.326469870313]
2288.9537498511854
"""