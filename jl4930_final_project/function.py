import numpy as np

def changeStringToFloat(data_string): #change string data into float
	num = len(data_string)
	dim = len(data_string[0])
	data = []

	for i in range(num):
		if(data_string[i][2]!=''):
			temp = []
			for j in range(2,dim): # actually, 2 to dim-1
				try:
					temp.append(float(data_string[i][j].replace(",","")))
				except ValueError:
					temp.append(0.0)
					print(i,'error line')
			data.append(temp)
	return data


def judgeIncrease(data): #find whether an array of data is increasing
	num = len(data)
	for i in range(num-1):
		if(data[i]<data[i+1]):
			return 0
	return 1

def abstractFeature(data): # normalize and process a given dataset
	num = len(data)
	dim = len(data[0])
	feature = []


	EarningsPerShares = []
	for i in range(num):
		temp = []
		for j in range(5):
			temp.append(data[i][j])
		EarningsPerShares.append(temp)

	NetProfitTotalAssetRatio = []
	for i in range(num):
		temp = []
		for j in range(5,10):
			temp.append( data[i][j]/(data[i][j+10]+data[i][j+15])*10 )
		NetProfitTotalAssetRatio.append(temp)
		
	OperatingProfitTotalAssetRatio = []
	for i in range(num):
		temp = []
		for j in range(10,15):
			temp.append( data[i][j]/(data[i][j+5]+data[i][j+10]) )
		OperatingProfitTotalAssetRatio.append(temp)

	NetAssetTotalAssetRatio = []
	for i in range(num):
		temp = []
		for j in range(15,20):
			temp.append( data[i][j]/(data[i][j]+data[i][j+5]) )
		NetAssetTotalAssetRatio.append(temp)

	NetProfitFirstYearRatio = []
	for i in range(num):
		temp = []
		firstYearNetProfit = data[i][9]
		for j in range(5,10):
			temp.append( data[i][j]/firstYearNetProfit*0.25)
		NetProfitFirstYearRatio.append(temp)

	OperatingProfitFirstYearRatio = []
	for i in range(num):
		temp = []
		firstYearOperatingProfit = data[i][14] + 0.1
		for j in range(10,15):
			temp.append( data[i][j]/firstYearOperatingProfit*0.25)
		OperatingProfitFirstYearRatio.append(temp)
	
	NetAssetFirstYearRatio = []
	for i in range(num):
		temp = []
		firstYearNetAsset = data[i][19]
		for j in range(15,20):
			temp.append( data[i][j]/firstYearNetAsset*0.25)
		NetAssetFirstYearRatio.append(temp)

	DebtFirstYearRatio = []
	for i in range(num):
		temp = []
		firstYearDebt = data[i][24]
		for j in range(20,25):
			temp.append( data[i][j]/firstYearDebt * 0.25)
		DebtFirstYearRatio.append(temp)
	
	NormalizedPrice = []
	for i in range(num):
		temp = []
		for j in range(25,30):
			temp.append(data[i][j]/50)
		NormalizedPrice.append(temp)

	NetProfitIncrease = []
	for i in range(num):
		NetProfitIncrease.append( [judgeIncrease(data[i][10:15])] )
		
	OperatingProfitIncrease = []
	for i in range(num):
		OperatingProfitIncrease.append( [judgeIncrease(data[i][15:20])] )
		
	CompanySize = []
	for i in range(num):
		totalAsset = data[i][15]+data[i][20]
		if(totalAsset<=100000):
			tempSize = 0.0/5.0
		elif(totalAsset<=1000000 and totalAsset>100000):
			tempSize = 1.0/5.0
		elif(totalAsset<=10000000 and totalAsset>1000000):
			tempSize = 2.0/5.0
		elif(totalAsset<=100000000 and totalAsset>10000000):
			tempSize = 3.0/5.0
		else:
			tempSize = 4.0/5.0
		CompanySize.append([tempSize])
	feature = np.hstack((EarningsPerShares, NetProfitTotalAssetRatio, OperatingProfitTotalAssetRatio, NetAssetTotalAssetRatio,
	NetProfitFirstYearRatio, OperatingProfitFirstYearRatio, NetAssetFirstYearRatio, DebtFirstYearRatio,NormalizedPrice,
	NetProfitIncrease,OperatingProfitIncrease, CompanySize))
	return feature

def generateLabel(data): #use price to generate label, 3 type of label 0,1,2
	num = len(data)
	dim = len(data[0])

	label = []
	label_combine = []

	for i in range(num):
		temp_label = 0
		max_price = np.max(data[i][25:30])
		min_price = np.min(data[i][25:30])
		price_2016 = data[i][30]
		
		point_1 = (max_price-min_price)/4+max_price
		point_2 = max_price
		point_3 = np.sum(data[i][25:30])/5
		#point_4 = min_price
		
		if (price_2016>point_1):
			temp_label = 3
		elif (price_2016>point_2 and price_2016<point_1):
			temp_label = 2
		elif (price_2016>point_3 and price_2016<point_2):
			temp_label = 1
		else:
			temp_label = 0
		label.append(temp_label)
		label_combine.append([temp_label])
		
	return label, label_combine

def generateLabel_test(data): #use price to generate label, 3 type of label 0,1,2
	num = len(data)
	dim = len(data[0])

	label = []
	label_combine = []

	for i in range(num):
		temp_label = 0
		max_price = np.max(data[i][25:30])
		min_price = np.min(data[i][25:30])
		price_2017 = data[i][30]
		
		point_1 = (max_price-min_price)/4 +max_price
		point_2 = max_price
		point_3 = np.sum(data[i][25:30])/5
		
		if (price_2017>point_1):
			temp_label = 3
		elif (price_2017>point_2 and price_2017<point_1):
			temp_label = 2
		elif (price_2017>point_3 and price_2017<point_2):
			temp_label = 1
		else:
			temp_label = 0
		label.append(temp_label)
		label_combine.append([temp_label])
		
	return label, label_combine