from csv import writer
from csv import reader
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import glob
import sys

def add_column_in_csv(input_file, output_file, transform_row):
  """ Append a column in existing csv using csv.reader / csv.writer classes"""
  # Open the input_file in read mode and output_file in write mode
  with open(input_file, 'r') as read_obj, \
          open(output_file, 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
      # Pass the list / row in the transform function to add column text for this row
      transform_row(row, csv_reader.line_num)
      # Write the updated row / list to the output file
      csv_writer.writerow(row)

def scanRaceGenderImagesAndGenerateDatabase(range_start, range_end):

    # read the created csv file containing all the paths
    df = pd.read_csv('_imagesPath.csv', delimiter = ",")

    # iterate 50 by 50 imaes and create csv files for them -> this is done to keep execution time short and to be able to create checkpoints
    for iteration in range(range_start, range_end):

        start = iteration*50
        end = (iteration+1)*50

        # intialize empty list containing race and gender scanned
        race_after_scan = []
        gender_after_scan = []

        # this is used to keep track which images we need to scan
        imgCnt = 0

        for index, row in df.iterrows():
            #print(str(row[0]))
            # increment counter until we get to the starting point image
            if(imgCnt < start):
                imgCnt = imgCnt + 1
                continue
            # if we reached the end image number, then stop the sacn and restart program with new argumetns to save time
            if(imgCnt == end):
                break
            print('## Image nr: ' + str(imgCnt))
            image_path = str(row[0])
            try: #some images may throw errors due to dimensions, mark those as unknown
                #print(image_path)
                # get the gender and race
                obj = DeepFace.analyze(img_path = image_path, actions = ['gender', 'race'])
                #print("#### ", obj["dominant_race"]," ", obj["gender"])
                race_after_scan.append(obj["dominant_race"])
                gender_after_scan.append(obj["gender"])
                imgCnt = imgCnt + 1
            except:
                race_after_scan.append('unknown_race')
                gender_after_scan.append('unknown_gender')
                imgCnt = imgCnt + 1
                continue

        # create csv files with the race and gender scanned
        header_of_new_col = "race_scan"
        header_of_new_col2 = "gender_scan"

        for race_i in race_after_scan:
            # print(race_i)
            # line_num - 2 because line_num starts at 1
            try:
                #add_column_in_csv('../databases/AdienceBenchmarkGenderAndAgeClassification/_dbInfo/db_fold_data.csv', '_output_buff.csv', lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(race_after_scan[line_num - 2]))
                add_column_in_csv('_dummy.csv', '_output_buff' + str(iteration) + '.csv', lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(race_after_scan[line_num - 2]))
            except:
                break

        for gender_i in gender_after_scan:
            # print(race_i)
            # line_num - 2 because line_num starts at 1
            try:
                add_column_in_csv('_output_buff' + str(iteration) + '.csv', '_final_output_' + str (start) + '_'+ str(end-1) +'.csv', lambda row, line_num: row.append(header_of_new_col2) if line_num == 1 else row.append(gender_after_scan[line_num - 2]))
            except:
                break

def getUniqueImages(images):

    unique_images = []

    for image_path_folder in images:
        for image_path in image_path_folder:
            unique_images.append(image_path)

    
    return unique_images

def createCsvFile(unique_images):

     with open("_imagesPath.csv", 'w', newline='') as write_obj:
         # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)

        for uniq_img in unique_images:
            # Write the updated row to the output file
            csv_writer.writerow(uniq_img)    
    

def createCsvWithImagesPath():

    #read the database provided by Adience Dataset
    df = pd.read_csv('../databases/AdienceBenchmarkGenderAndAgeClassification/_dbInfo/db_fold_data.csv', delimiter = ",")

    ### initialize empty lists ###
    # this will be a lost of lists that contain all the image paths
    images_temp = []
    # this will be a simple list that will contain all images path
    unique_images = []

    for index, row in df.iterrows():
        #row[0] = user_id, row[1] = original_image
        local_download_path = '../databases/AdienceBenchmarkGenderAndAgeClassification/_adienceDbFolder/' + row[0]
        # use regex expressions to get a list of all paths that match
        images_buffer = glob.glob(local_download_path + '/*' + row[1])
        # append this list to the images_temp list
        images_temp.append(images_buffer)

    # get the unique images from image_temp which is a list of lists
    unique_images = getUniqueImages(images_temp)

    print('### Images AFTER getting them filterd')

    #for uniq_img in unique_images:
    #    print(str(uniq_img))

    print(len(images_temp))
    print(len(unique_images))

    # create _imagesPath.csv file with paths contained by unique_images list
    createCsvFile(unique_images)

def main():
    print('Hello Mom!')

    #Get arguments from commandline
    range_start =  int(sys.argv[1])
    range_end = int(sys.argv[2])

    # print(range_start)
    # print(range_end)

    #createCsvWithImagesPath() # -> create the CSV file that will contain the path to all images: _imagesPath.csv
    scanRaceGenderImagesAndGenerateDatabase(range_start, range_end) # -> scan all images from the _imagesPath.csv file and get the race and gender




if __name__ == "__main__":
    main()