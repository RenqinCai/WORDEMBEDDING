import numpy as np
import random

def transformItemFrequencyMap(itemFrequencyMap, powerParam):
	totalFrequency = 0
	for itemIndex in itemFrequencyMap.keys():
		itemFrequency = itemFrequencyMap[itemIndex]

		transformedItemFrequency = np.power(itemFrequency, powerParam)
		itemFrequencyMap[itemIndex] = transformedItemFrequency

		totalFrequency += transformedItemFrequency

	for itemIndex in itemFrequencyMap.keys():
		itemFrequency = itemFrequencyMap[itemIndex]

		itemFrequencyMap[itemIndex]  = itemFrequency*1.0/totalFrequency


def negativeSampling(positiveItem, samplingSize, itemFrequencyMap):
	sampleIndexList = []
	itemList = itemFrequencyMap.keys()

	for samplingIndex in range(samplingSize):
		itemIndex = unigramSampling(samplingIndex, positiveItem, itemList, itemFrequencyMap)

		if itemIndex == positiveItem:
			print "repeat positiveItem"
			itemIndex = unigramSampling(samplingIndex, positiveItem, itemList, itemFrequencyMap)
		
		sampleIndexList.append(itemIndex)

	return sampleIndexList

def unigramSampling(samplingIndex, positiveItem, itemList, itemFrequencyMap):
	randomProb = random.random()
	sampledItemIndex = 0
	for item in itemList:
		itemFrequencyProb = itemFrequencyMap[item]

		randomProb -= itemFrequencyProb

		if randomProb < 0:
			print "%d round sampling done---->\t"%samplingIndex
			sampledItemIndex = item

			return sampledItemIndex


positiveItemIndex = 4
samplingSize = 5
itemFrequencyMap = {1:3, 4:5, 6:2, 2:9, 7:8, 10:88, 13:24, 48:50, 77:67, 89:39}

powerParam = 3/4

transformItemFrequencyMap(itemFrequencyMap, powerParam)

sampledItemList = negativeSampling(positiveItemIndex, samplingSize, itemFrequencyMap)

print "sampledItemList\t", sampledItemList