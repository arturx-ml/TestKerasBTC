import bitmex
import curl
import  pandas as pd
c = curl.Curl()
with open('/home/arturx/btchourly.json', 'w') as file:
    for i in range(1):
        d = c.get(url='https://testnet.bitmex.com/api/v1/quote/bucketed',
                  params={'binSize': '1h', 'symbol': 'XBTUSD', 'partial': 'false', 'start': 500 * i, 'count': 500,
                          '_format': 'csv'})

        # d = d.replace('b\'', '')
        # d = d.replace(']\'b\'[', ',')
        # # d = d.replace('[', '')
        # # d = d.replace(']', '')
        # file.writelines(d)
