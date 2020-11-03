#import pandas as pd
from pandas import pandas as pd
#from google_images_download import google_images_download
import os
import json


#pip install git+https://github.com/Joeclinton1/google-images-download.git





#Reads a CSV file and returns the data
def read_CSV_File(csvName, seperator):

    data = pd.read_csv(csvName, sep=seperator, header=None)
    
    return data


#Get all user ID codes
#def getUserIDs()




#Takes in a search word and returns all dishes that contains word as json object and a list of names
def searchDish(searchString):

    data = read_CSV_File('item-profiles2.csv', ';')

    #names = []
    dictList = []

    for i in data.index:

        matchedIDs = {}

        val = data.iloc[i]

        print('value: ', val[1])

        if searchString.lower() in val[1].lower():
            
            matchedIDs['label'] = val[1]
            matchedIDs['value'] = val[0]

            dictList.append(matchedIDs)
            #matchedIDs[val[1]] = val[0]
            #names.append(val[1])
        
    #print(matchedIDs)

    jsonObject = json.dumps(dictList)

    print(jsonObject)

    return jsonObject

        



#Takes a user and return a list of names for their rated dishes in rating based descending order
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

    dictList = []

    #recipeNames = []

    for x in userValues:

        matchedIDs = {}
        
        #print(x[1][2])
        matchedIDs['value'] = x[1][2]

        for y in data.index:
        
            valY = data2.iloc[y]


            if str(x[1][2]) == valY[0]:

                #print(valY[1])
                matchedIDs['label'] = valY[1]
                dictList.append(matchedIDs)
                #recipeNames.append(valY[1])
                break

    jsonObject = json.dumps(dictList)

    #print(jsonObject)

    return jsonObject
    #return recipeNames

    

'''
#Take a list of names and downloads an image from google images for each name in the list, returns list with paths of the images
def downloadRecipeImages(recipeNamesList):
    
    imagePaths = []
    for name in recipeNamesList:

        try:
            name = name.replace(',','')

            response = google_images_download.googleimagesdownload()

            arguments = {"keywords":name,"limit":1,"print_urls":True, "no_directory":True, "size":"large"}
            paths = response.download(arguments)

            oldName = paths[0][name][0].split('\\')[5]

            if '.jpg' or '.JPG' in oldName:
                newName = name+'.jpg'

            elif '.png' or '.PNG' in oldName:
                newName = name+'.png'
            else:
                print(name, ' Has wrong format')
                continue

            newPath = paths[0][name][0].replace(oldName, '') + newName
            os.rename(paths[0][name][0], newPath)

            imagePaths.append(newPath)

    return imagePaths

        except:
            pass
'''


#############################################################################################################    


#Get recipes and download their image
'''
recipeNameList = findTopDishes(455)
paths = downloadRecipeImages(recipeNameList)
'''

#Search for recipes and download images
'''
jsonData, names = searchDish('pizza')
paths = downloadRecipeImages(names)
'''








#Backup of old functions

########################################
def read_BMJDataALL(csvName, x):

    data = pd.read_csv(csvName, sep='\t')

    val = data.iloc[x]

    dishName = val['Name']
    
    return dishName



def downloadRecipeImagesOld():
    
    data =read_CSV_File('BMJ-data-all--b-new.csv', '\t')

    temp = []

    for x in range(0, len(data)):

        try:
            name = read_BMJDataALL('BMJ-data-all--b-new.csv', x)

            name = name.replace(',','')

            response = google_images_download.googleimagesdownload()

            arguments = {"keywords":name,"limit":1,"print_urls":True, "no_directory":True, "size":"large"}
            paths = response.download(arguments)

            oldName = paths[0][name][0].split('\\')[5]

            if '.jpg' or '.JPG' in oldName:
                newName = name+'.jpg'

            elif '.png' or '.PNG' in oldName:
                newName = name+'.png'
            else:
                print(name, ' Has wrong format')
                continue

            temp.append(name)

            newPath = paths[0][name][0].replace(oldName, '') + newName
            os.rename(paths[0][name][0], newPath)
        except:
            pass



def findTopDishesOld(userCode):

    dictList = []
    
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


    recipeNames = []

    for x in userValues:
        #print(x[1][2])

        for y in data.index:
        
            valY = data2.iloc[y]


            if str(x[1][2]) == valY[0]:

                #print(valY[1])
                recipeNames.append(valY[1])
                break

    return recipeNames












