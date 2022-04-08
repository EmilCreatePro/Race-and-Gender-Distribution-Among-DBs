import pandas as pd
from createDB import add_column_in_csv
from csv import writer
from csv import reader

def joinGeneratedDatabases():

    race_after_scan = []
    gender_after_scan = []

    header_of_new_col = "race_scan"
    header_of_new_col2 = "gender_scan"

    imageIndex = 0

    for fileIndex in range(0, 878):

        start = fileIndex*50
        end = (fileIndex+1)*50

        df = pd.read_csv('_scanImages/_final_output_' + str (start) + '_'+ str(end-1) +'.csv', delimiter = ",")
        
        for index, row in df.iterrows():
            #print('## Image index: ' + str(imageIndex))
            print(row[0] + ', ' + row[1] + ', ' + row[2])
            
            race_after_scan.append(row[1])
            gender_after_scan.append(row[2])

            imageIndex = imageIndex + 1

    print('## Nr of images: ' + str(imageIndex))

    imgCnt = 0
    
    for race_i in race_after_scan:
        # print(race_i)
        # line_num - 2 because line_num starts at 1
        try:
            #add_column_in_csv('../databases/AdienceBenchmarkGenderAndAgeClassification/_dbInfo/db_fold_data.csv', '_output_buff.csv', lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(race_after_scan[line_num - 2]))
            add_column_in_csv('_imagesPath.csv', '_output_buff.csv', lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(race_after_scan[line_num - 2]))
            print('Appending race img ' + str(imgCnt))
            imgCnt = imgCnt + 1
        except:
            break

    imgCnt = 0
    for gender_i in gender_after_scan:
        # print(race_i)
        # line_num - 2 because line_num starts at 1
        try:
            add_column_in_csv('_output_buff.csv', '_final_output_race_gender.csv', lambda row, line_num: row.append(header_of_new_col2) if line_num == 1 else row.append(gender_after_scan[line_num - 2]))
            print('Appending gender img ' + str(imgCnt))
            imgCnt = imgCnt + 1
        except:
            break

def main():
    print('Hello Mom 2!')

    joinGeneratedDatabases()



if __name__ == "__main__":
    main()