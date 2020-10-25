import pandas as pd
from google_images_download import google_images_download

#pip install git+https://github.com/Joeclinton1/google-images-download.git


'''
def read_ItemProfiles(csvName):

    data = pd.read_csv(csvName, sep=';')

    print(data)
    print(data.to_string())

'''




def read_CSV_File(csvName, seperator):

    data = pd.read_csv(csvName, sep=seperator, header=None)
    
    return data





'''
def read_BMJDataALL(csvName):

    data = pd.read_csv(csvName, sep='\t')

    val = data.iloc[0]

    print(val)

    #print(val['Name'])

    dishName = val['Name']

    
    return dishName
'''






def searchDish(searchString):

    data = read_CSV_File('item-profiles2.csv', ';')
    
    matchedIDs = []
    
    for i in data.index:
    
        val = data.iloc[i]

        if searchString.lower() in val[1].lower():
            matchID.append(val[0])

    print(matchedIDs)

    return matchedIDs

        






def findTopDishes(userCode):
    
    data = read_CSV_File('user-item-rating.csv', '\t')
    data2 = read_CSV_File('item-profiles2.csv', ';')

    count = 0

    userValues = {}
    
    for i in data.index:
    
        val = data.iloc[i]
        
        if int(val[0]) == int(userCode):
            
            userValues[count] = int(val[0]), val[2], int(val[1])
            count = count + 1
            

    userValues = sorted(userValues.items(), key=lambda x: x[1], reverse=True)


    matchedIDs = []

    for x in userValues:
        print(x[1][2])


        for y in data.index:
        
            valY = data2.iloc[y]


            if str(x[1][2]) == valY[0]:

                print(valY[1])
                break










#############################################################################################################    




findTopDishes(455)

#searchDish('pizza')






    


#read_ItemProfiles('item-profiles3.csv')

#Download recipe image
'''
name = read_BMJDataALL('BMJ-data-all--b-new.csv')




try:
    name = read_BMJDataALL('BMJ-data-all--b-new.csv', x)


    response = google_images_download.googleimagesdownload()

    arguments = {"keywords":name,"limit":1,"print_urls":True, "no_directory":True}
    paths = response.download(arguments)
    print(paths)
except:
    pass
'''

