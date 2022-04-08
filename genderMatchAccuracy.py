import pandas as pd

def main():
    print('Hello Mom 5!')

    test1 = 'Man'
    test12 = 'Woman'
    test13 = 'unknown_gender'
    test2 = 'm'
    test3 = 'f'

    maleMatches = 0
    maleMisMatches = 0
    femaleMatches = 0
    feamleMisMatches = 0

    #read the 2 excel files
    groundTruthInfoCSV = pd.read_csv('../databases/AdienceBenchmarkGenderAndAgeClassification/_dbInfo/db_fold_data.csv', delimiter = ",")
    scannedGenderCSV = pd.read_csv('_finalGenderRaceDB/_final_gender_race_DB.csv', delimiter = ",")

    testCnt = 0

    alreadyCheckedCnt = 0


    for indexGT, rowGT in groundTruthInfoCSV.iterrows():
        for indexS, rowS in scannedGenderCSV.iterrows():
            #startCnt = 0
            #if(startCnt <= alreadyCheckedCnt):
            #    startCnt = startCnt + 1
            #    continue
            # if we find the row substring from the database in our final database, check the gender
            if (rowGT[1] in rowS[0]):
                if(rowGT[4] == 'm'):
                    if(rowS[2] == 'Man'):
                        maleMatches = maleMatches + 1
                    else:
                        maleMisMatches = maleMisMatches + 1
                elif(rowGT[4] == 'f'):
                    if(rowS[2] == 'Woman'):
                        femaleMatches = femaleMatches + 1
                    else:
                       feamleMisMatches = feamleMisMatches + 1 

                break
            
            #alreadyCheckedCnt = alreadyCheckedCnt + 1

            
        print('maleMatches = ' + str(maleMatches) )
        print('maleMisMatches = ' + str(maleMisMatches) )
        print('femaleMatches =  '+ str(femaleMatches) )
        print('feamleMisMatches = ' + str(feamleMisMatches) )

            #if(testCnt == 100):
            #    return

    print('##################################')
    print('maleMatches = ' + str(maleMatches) )
    print('maleMisMatches = ' + str(maleMisMatches) )
    print('femaleMatches =  '+ str(femaleMatches) )
    print('feamleMisMatches = ' + str(feamleMisMatches) )

if __name__ == "__main__":
    main()