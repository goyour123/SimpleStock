import sys, os
import json

if __name__ == '__main__':

  argNames = ['Script']
  args = dict(zip(argNames, sys.argv))
  cfgName = args['Script'].split('.')[0]
  cfgExt = 'json'

  try:
      with open (cfgName + '.' + cfgExt, 'r') as j:
          cfg = json.load(j)
  except:
      sys.exit()

  taxRate = cfg["Tax_Rate"]
  feeRate = cfg["Fee_Rate"]
  feeMinPrice = cfg["Fee_Min_Price"]
  lotUnit = cfg["Lot_Unit"]

  for stock in cfg['Stock']:
    cost = 0
    totalQty = 0
    for item in cfg['Stock'][stock]:
      price = cfg['Stock'][stock][item]['price']
      qty = cfg['Stock'][stock][item]['quantity']
      fee = int (price * qty * feeRate if (price * qty * feeRate) > feeMinPrice else feeMinPrice)

      cost += int (price * qty + fee)
      totalQty += qty

    totalLot = int (totalQty / lotUnit)

    breakEvenFee = cost * / totalLot
    breakEvenPrice = (cost / (totalLot * lotUnit * (1 - taxRate - feeRate)))

    print (breakEvenPrice)
