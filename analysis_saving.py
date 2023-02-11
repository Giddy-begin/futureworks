import pandas as pd
from analysis_degrading import GetAmountOfSaveResources

class Saving(GetAmountOfSaveResources):
    
    def __init__(self, userCSVPath: str, ingredientsCSVPath: str, degradingTimeCSVPath: str, savePath: str):
        self.concatAmountSavings(userCSVPath, ingredientsCSVPath, degradingTimeCSVPath, savePath)
        
    def amountSaving(self, userCSVPath: str):
        map = self.getMapFromCSV(userCSVPath)
        res = self.getSumRow(map)
        return res
    
    def concatAmountSavings(self, userCSVPath, ingredientsCSVPath: str, degradingTimeCSVPath: str, savePath: str):
        res = self.amountSaving(userCSVPath)
        degTimeMap = self.getDegTimeEach(ingredientsCSVPath, degradingTimeCSVPath, userCSVPath, savePath)
        map = {}
        for k, v in res.items():
            
            if k not in map.keys():
                map[k] = []
            list = [str(round(3781*v[0], 3)), str(round(0.00461956521*v[0], 3)), str(round(0.00000461956*v[0], 3)), str(round(0.3429565217*v[0], 3)), f"{v[0]}/108235294118"]
            for l in list:
                map[k].append(l)
        for k, v in degTimeMap.items():
            map[k].append(v)
        print(map)
        self.printMap(map)
        return map
    
    def printMap(self, map: map):
        for k, v in map.items():
            print(f"water required (L): {v[0]}")
            print(f"value saved from wasting ($): {v[1]} ")
            print(f"reduced micro fivers (tonnes): {v[2]}")
            print(f"reduced carbon emission (metric tonnes): {v[3]}")
            print(f"user{k} saved amount of clothes: {v[4]}")
            print(f"user{k} saved degrading time of ingredients of Clothes (month): {v[5]}\n" )

    
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
        _, degradingTimeTotalMap = self.getSum(ingredientsCSVPath, degradingTimeCSVPath, savePath)
        userMap = self.getMapFromCSV(userCSVPath)
        df = self.getCSV(userCSVPath)
        userCols = df.keys()
        savingTimeMap = {}
        for k in userMap.keys():
            values = userMap[k]
            for i, v in enumerate(userCols[1:]):
                if v in degradingTimeTotalMap.keys():
                    timeSaving = values[i] * degradingTimeTotalMap[v]
                    if k not in savingTimeMap.keys():
                        savingTimeMap[k] = []
                    savingTimeMap[k].append(round(timeSaving, 4))
        
        total = 0
        resMap = {}
        for k in savingTimeMap.keys():
            for v in savingTimeMap[k]:
                total += v
            resMap[k] = round(total, 3)
            
        return resMap

        
            
if __name__=="__main__":
    obj = Saving("./random_user.csv", "./test4.csv", "./result.csv", "./save.csv")
    