#library for the matching algorithm
from thefuzz import fuzz, process
#library to open and read the csv file provided
import csv

#Class for the matching and geting the result 
class Stations:
    def __init__(self, dir):
        self.suggestions = {}
        file=open(dir)
        reader= csv.reader(file)
        data=list(reader)
        self.stations= {}    
        for x in list(range(0,len(data))):
            self.stations[data[x][0].lower()]= data[x][1].lower()

    #the matching algorithm (the usage of fuzz here) 
    def match(self,choice):
        suggestion={}
        for i,j in self.stations.items():  
            #checking the similar station names or abbrevations above 80 percent
            if fuzz.partial_ratio(choice,i)>80 or fuzz.ratio(choice,i)>80:
                suggestion[i]=j
            if fuzz.partial_ratio(choice,j)>80 or fuzz.ratio(choice,j)>80:
                suggestion[j]=i

        self.suggestions=suggestion          

        if len(self.suggestions)>0:
                return self.suggestions.keys()
        else: 
            return "Not Found !"



#algorithm I have use showing the final results after selection
    def get_result(self,word):
        if word in self.suggestions.keys():
            return self.suggestions.get(word)
        elif word in self.suggestions:
            return self.suggestions.keys()
    






