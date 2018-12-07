import json
import requests

currentStock = requests.get("https://ca.desknibbles.com/products.json?limit=250")
snackerListResp = requests.get("https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json")

stockJsonData = currentStock.json()["products"]
snackerListJson = snackerListResp.json()

productStock = {}
for cont in stockJsonData:
  if cont["title"] not in productStock: productStock[cont["title"]] = cont

snacksStocked = []
snackerEmail = []
totalSnackerPrice = 0
for snacker in snackerListJson:
  if snacker["fave_snack"] in productStock:
    print("{}: {}".format(snacker["email"], snacker["fave_snack"]))
    totalSnackerPrice += float(productStock[snacker["fave_snack"]]["variants"][0]["price"])
print()
print("Total Price: {}".format(totalSnackerPrice))