'''
Attemps to cast things to dictionary, never actual use this, just copy and paste
'''


def dict_itemised_string(data, item_delimiter, key_delimiter):
   return dict([item.strip().split(key_delimiter) for item in data.split(item_delimiter) if item])


data = "SID=DQAAAG9AADKIZ2o7NSDF382ssd---GtwkkTvi0x0FA \n\
        LSID=DQAAAG9ArdrZg97VrbuPx9TKn---nsxJ1oeUX41 \n\
  		Auth=AIwbFARksypDdUSGGYRI_5v7Z---OC-I1VJtQ"


print dict_itemised_string(data, "\n","=")