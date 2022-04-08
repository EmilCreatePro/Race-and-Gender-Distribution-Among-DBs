import pandas as pd

def getSepcificRaceGenderNumbers(race_list, gender_list, race_el, gender_el):

    elements_cnt = 0

    for i in range(0, len(race_list)):
        if(race_list[i] == race_el and gender_list[i] == gender_el):
            elements_cnt = elements_cnt + 1

    print("For " + race_el + " and " + gender_el + " we have: " + str(elements_cnt))


def extractData():
    df = pd.read_csv('_finalGenderRaceDB/_final_gender_race_DB.csv', delimiter = ",")
    
    race_scan = []
    gender_scan = []

    #create sets to store unique values, init them with unknown races/genders
    race_set = {'unknown_race'}
    gender_set = {'unknown_gender'}

    for index, row in df.iterrows():
        #print(row[0] + ' ' + row[1] + ' ' + row[2])
        race_scan.append(row[1])
        gender_scan.append(row[2])

    
    latino_hispanic_cnt = 0
    indian_cnt = 0 
    black_cnt = 0 
    white_cnt = 0 
    asian_cnt = 0 
    middle_eastern_cnt = 0 
    unknown_race_cnt = 0
    
    woman_cnt = 0
    man_cnt = 0
    unknown_gender_cnt = 0

    # count the ethnicity and gender for each person
    for race_i in race_scan:
        #print(race_i)
        # create set beacuse elements are unique in a set
        race_set.add(race_i) #add to the race set

        # increment the counters
        if(race_i == 'latino hispanic'):
            latino_hispanic_cnt = latino_hispanic_cnt + 1
        if(race_i == 'indian'):
            indian_cnt = indian_cnt + 1
        if(race_i == 'black'):
            black_cnt = black_cnt + 1
        if(race_i == 'white'):
            white_cnt = white_cnt + 1
        if(race_i == 'asian'):
            asian_cnt = asian_cnt + 1
        if(race_i == 'middle eastern'):
            middle_eastern_cnt = middle_eastern_cnt + 1
        if(race_i == 'unknown_race'):
            unknown_race_cnt = unknown_race_cnt + 1

    for gender_i in gender_scan:
        #print(gender_i)
        gender_set.add(gender_i) #add to the gender set
        # increment the counters
        if(gender_i == 'Woman'):
            woman_cnt = woman_cnt + 1
        if(gender_i == 'Man'):
            man_cnt = man_cnt + 1
        if(gender_i == 'unknown_gender'):
            unknown_gender_cnt = unknown_gender_cnt + 1
    
    '''
    print(len(race_scan))
    print(len(gender_scan))
    '''
    print('Races are:', race_set)
    print('Genders are:', gender_set)

    print("latino_hispanic_cnt: " + str(latino_hispanic_cnt))
    print("indian_cnt: " + str(indian_cnt))
    print("black_cnt: " + str(black_cnt))
    print("white_cnt: " + str(white_cnt))
    print("asian_cnt: " + str(asian_cnt))
    print("middle_eastern_cnt: " + str(middle_eastern_cnt))
    print("unknown_race_cnt: " + str(unknown_race_cnt))
    print("woman_cnt: " + str(woman_cnt))
    print("man_cnt: " + str(man_cnt))
    print("unknown_gender_cnt: " + str(unknown_gender_cnt))

    # get all possible combinations for them
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'latino hispanic', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'indian', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'black', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'white', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'asian', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'middle eastern', "Man")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'unknown_race', "Man")

    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'latino hispanic', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'indian', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'black', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'white', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'asian', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'middle eastern', "Woman")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'unknown_race', "Woman")

    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'latino hispanic', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'indian', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'black', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'white', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'asian', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'middle eastern', "unknown_gender")
    getSepcificRaceGenderNumbers(race_scan, gender_scan, 'unknown_race', "unknown_gender")

    return


def main():
    print('Hello Mom 4!')

    extractData()



if __name__ == "__main__":
    main()