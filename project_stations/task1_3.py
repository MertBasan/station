#csv file library
import csv 
#library for multiprocessing(handling data separetely)
import multiprocessing as mp




def multiple_station_finder(input):
    #printing the output in another file
    output=open('results.csv',"a+")

    
    for data in input:
        file=open('railway_stations.csv',"r")
        reader= csv.reader(file)
        print(data)

        for line in reader:
            if line[0].lower()== data[0].lower():
                output.write(line[1])
                output.write("\n")
                break   
            elif line[1].lower()== data[0].lower():
                output.write(line[0])
                output.write("\n")
                break
                
        else:
            print("Not Found !")



def parallelisedSearch(text):
    n = 4 # number of processes
    
    steps = len(text)//n   # size of each portion for the given csv file
    text="task 1_3 testing data.csv"

    processes=[]
    for i in range(n-1):
        x=[]
        with open('task 1_3 testing data.csv') as csv_file:
            data=csv.reader(csv_file)
            x=list(data)[i*steps:(i+1)*steps]
            processes.append(mp.Process(target= multiple_station_finder, args=(x,)))
        


    with open('task 1_3 testing data.csv') as csv_file:
        data = csv.reader(csv_file)
        x = list(data) [(n-1)*steps::]


    processes.append(mp.Process(target=multiple_station_finder,args=(x,)))
    return processes




if __name__=="__main__":
    
    processes=parallelisedSearch("task 1_3 testing data.csv")
    #method starts the process
    for p in processes:
        p.start()
    #method to wait until other processoe finishes
    for p in processes:
        p.join()











































# def serialSearch(file, index):
#     found = False        
#     for lineno in range(len(file)):
#         #str.find(pattern) returns the position of the pattern in the string and returns -1 if no match
#         if file[lineno].find('Ludlow') != -1:
#             print("Found the keyword in line "+str(index + lineno+1))
#             found = True
#             break
    
#     if found is False:
#         print("The text didn't contain this keyword!")  



# def parallelisedSearch(pattern, file):
#     n = 4 # number of processes
    
#     steps = len(file)//n   # size of each portion for the text file
    
#     # first three processes get the equal portion of the text
#     processes = [mp.Process(target=serialSearch, args=(pattern,file[i*steps:(i+1)*steps:],i*steps)) for i in range(n-1)]
#     # add the last one which might have a different size of text
#     processes.append(mp.Process(target=serialSearch, args=(pattern,file[(n-1)*steps::],(n-1)*steps)))
    
#     for p in processes:
#         p.start()
        
#     for p in processes:
#         p.join()








