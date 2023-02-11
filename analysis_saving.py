import pandas as pd
from analysis_degrading import GetAmountOfSaveResources

class Saving(GetAmountOfSaveResources):
    
    def __init__(self, userCSVPath):
        self.printAmountSaving(userCSVPath)
        
    def printAmountSaving(self, userCSVPath):
        map = self.getMapFromCSV(userCSVPath)
        res = self.getSumRow(map)
        print(res)
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
        
        print(sumMap)
        return sumMap
            
if __name__=="__main__":
    obj = Saving("./random_user.csv")
    