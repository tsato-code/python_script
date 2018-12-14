"""
quadkeyのテスト
pip install mercantile
"""
import mercantile


print(help(mercantile))


lat =  35.681166
lon = 139.766992
depth = 10
# 位置情報からタイルの取得
print(mercantile.tile(lon, lat, depth))
# タイルから左上の位置情報取得
print(mercantile.ul(mercantile.tile(lon, lat, depth)))
# タイルから1次元キー取得
print(mercantile.quadkey(mercantile.tile(lon, lat, depth)))
# キーから位置情報取得
print(mercantile.quadkey_to_tile(mercantile.quadkey(mercantile.tile(lon, lat, depth))))
# 位置情報からsphere xyを取得
print(mercantile.xy(lon, lat, depth))