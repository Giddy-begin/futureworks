import pandas as pd

class GetAmountOfSaveResources():
    
    def getMapFromCSV(self, filePath: str):
        df = self.getCSV(filePath)
        map = self.makeMapFromDF(df)
        return map

    def getCSV(self, filePath: str):
        df = pd.read_csv(filePath)
        return df
    
    def makeMapFromDF(self, df):
        rows = df.index
        columns = df.columns
        map = {}
        for r in rows:
            for c in columns:
                if r not in map.keys():
                    map[r] = []
                
                try:
                    df.loc[r]
                    df.loc[r,c]
                except:
                    print("Error Occurred in DataFrame")
                    return
                map[r].append(float(df.loc[r, c]))
        return map
    
    def calculate(self, map: map, averageResourceMap: map):
        mapOfSaveResource = {}
        
        for k in map.keys():
            for v in averageResourceMap.values():
                try:
                    map[k]
                except:
                    print(f"{k} is not a key in map")
                for prop in map[k]:
                    for deg in v:
                        saveAmount = prop * deg * 0.01
                    if k not in mapOfSaveResource.keys():
                        mapOfSaveResource[k] = []
                    mapOfSaveResource[k].append(saveAmount)
        return mapOfSaveResource
    
    def getSum(self, ingredientsCSVPath: str, degradingTimeCSVPath: str, savePath: str):
        ingMap = self.getMapFromCSV(ingredientsCSVPath)
        degMap = self.getMapFromCSV(degradingTimeCSVPath)
        resMap = self.calculate(ingMap, degMap)
        sumMap = {}
        res = 0.0
        for k in resMap.keys():
            for v in resMap[k]:
                res += v
            sumMap[k] = res
            res = 0.0
            
        df = pd.json_normalize(sumMap)
        csv = df.to_csv(savePath)
        return csv, sumMap
    
        
if __name__=="__main__":
    obj = GetAmountOfSaveResources()
    res, _ = obj.getSum("./test4.csv", 
                    "./test3.csv",
                    "./result.csv"
                    )