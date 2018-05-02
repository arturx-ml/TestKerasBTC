import pandas as pd

df = pd.read_csv(
    'https://testnet.bitmex.com/api/v1/quote/bucketed?binSize=1d&partial=false&symbol=XBTUSD&columns=timestamp%2CbidSize%2CaskSize%2CbidPrice%2CaskPrice&count=10&reverse=true&_format=csv')
df.to_csv('/home/arturx/text.csv',index=False)
# with open('/home/arturx/btchourly.json', 'r') as f:
#     data = f.readlines()
#
# # remove the trailing "\n" from each line
# # print (data)
#
# # data = map(lambda x: x.rstrip(), data)
# # each element of 'data' is an individual JSON object.
# # i want to convert it into an *array* of JSON objects
# # which, in and of itself, is one large JSON object
# # basically... add square brackets to the beginning
# # and end, and have all the individual business JSON objects
# # separated by a comma
# print (str(data))
# data_json_str = "[" + ','.join(str(data)) + "]"
#
# # now, load it into pandas
# print (data_json_str)
# df = pd.read_json(data_json_str)
#
# df.to_csv('/home/arturx/btc1h.csv',index=False)
