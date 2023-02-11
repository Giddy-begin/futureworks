import pandas as pd
from analysis_degrading import GetAmountOfSaveResources

class Saving(GetAmountOfSaveResources):
    
    def __init__(self, userCSVPath):
        # self.printAmountSavings(userCSVPath)
        self.getDegTimeEach("./test4.csv", "./result.csv", "./random_user.csv", "./time_savings.csv")
        
    def amountSaving(self, userCSVPath):
        map = self.getMapFromCSV(userCSVPath)
        res = self.getSumRow(map)
        return res
    
    def printAmountSavings(self, userCSVPath):
        res = self.amountSaving(userCSVPath)
        for k, v in res.items():
            print(f"water required (L): {3781 * v[0]}")
            print(f"value saved from wasting ($): {0.00461956521 * v[0]} ")
            print(f"reduced micro fivers (tonnes): {0.342956217 * v[0]}")
            print(f"reduced carbon emission (metric tonnes): {0.3429565217 * v[0]}")
            print(f"user{k} saved {v[0]} amount of clothes out of 108235294118\n")
    
    def getSumRow(self, map: map):
        sum = 0
        sumMap = {}
        for k in map.keys():
            for v in map[k]:
                sum += v
            if k not in sumMap.keys():
                sumMap[k] = []
            sumMap[k].append(int(sum))
        
        return sumMap
    
    def getDegTimeEach(self, ingredientsCSVPath: str, degradingTimeCSVPath: str, userCSVPath: str, savePath: str):
        _, sumMap = self.getSum(ingredientsCSVPath, degradingTimeCSVPath, savePath)
        userMap = self.getMapFromCSV(userCSVPath)
        savingTimeMap = {}
        print(userMap.keys())
        for k in userMap.keys():
            values = userMap[k]
            print(values)
            for v in values:
                timeSaving = v * sumMap[k]
                print(timeSaving)
                savingTimeMap[k] = round(timeSaving, 4)
        print(savingTimeMap)

        
            
if __name__=="__main__":
    obj = Saving("./random_user.csv")
    