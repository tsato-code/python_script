"""
緯度経度を文字列にエンコード、デコード
pip install geohash2
"""
import geohash2


lat =  35.681166
lon = 139.766992
enc = geohash2.encode(lat, lon, precision=8)
dec = geohash2.decode(enc)
dec_e = geohash2.decode_exactly(enc)

print('Geohash for {}, {}: {}'.format(lat, lon, enc))
print('Coordinate for Geohash {}: {}'.format(enc, dec))
print('Coordinate for Geohash {}: {}'.format(enc, dec_e))