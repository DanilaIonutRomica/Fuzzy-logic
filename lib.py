import pandas as pd 
import numpy as np 

#count function
def countYesAndNoM(matrix,column_index,dim_column,instance):
    yes_count=0
    no_count=0
    for i in range(0,dim_column):
        if matrix[i][column_index] ==instance and matrix[i][-1] == "Yes":
            yes_count+=1
        if matrix[i][column_index] ==instance and matrix[i][-1] == "No":
            no_count+=1
    return [yes_count,no_count]

#calcultate the entropy for the entire dataset
def calculate_entropy_for_entire_matrix(matrix,dim_column):
    yes_count=0
    no_count=0
    for i in range(0,dim_column):
        if matrix[i][-1] == "Yes":
            yes_count+=1
        if matrix[i][-1] == "No":
            no_count+=1
    if yes_count == 0 or no_count == 0:
        totalEntropy=0
    else:
        totalEntropy=-yes_count/(yes_count+no_count)*np.log2(yes_count/(yes_count+no_count))-no_count/(yes_count+no_count)*np.log2(no_count/(yes_count+no_count))
    return totalEntropy

#does calculate entropy for instance
def calculate_entropy_for_instanceM(numberYes,numberNo, numberOfTotalInstances):
    if numberYes == 0 or numberNo == 0:
        totalEntropy=0
    else:
        totalEntropy=-numberYes/(numberYes+numberNo)*np.log2(numberYes/(numberYes+numberNo))-numberNo/(numberYes+numberNo)*np.log2(numberNo/(numberYes+numberNo))
    return totalEntropy*(numberYes+numberNo)/numberOfTotalInstances

#calculate entropy for instance
def return_entropy_for_instance(matrix,dim_column,column_index,instance):
    yesAndNo=countYesAndNoM(matrix,column_index,dim_column,instance)
    return calculate_entropy_for_instanceM(yesAndNo[0],yesAndNo[1],dim_column)

#calculates the information gain
def information_gain(matrix,dim_column,column_index, list_of_avalable_instances):
    entropy_of_the_caracteristic=0
    for element in list_of_avalable_instances:
        entropy_of_the_caracteristic+=return_entropy_for_instance(matrix,dim_column,column_index,element)
    return calculate_entropy_for_entire_matrix(matrix,dim_column)-entropy_of_the_caracteristic

#returns a new matrix in witch the caracteristic that is split by is deleted and any row that has that instance of split is keeped
def split_matrix_after_instance(original_matrix,dim_row,dim_column,instance_of_split,column_index=None):
    if column_index == None:
        list_of_indexs=[]
        for i in range(0,dim_row):
            for j in range(0,dim_column):
                if original_matrix[i][j] == instance_of_split:
                    list_of_indexs.append(i)
        return_matrix=[]
        for elem in list_of_indexs:
            list_elements_in_a_row=[]
            for j in range(0,dim_column):
                if original_matrix[elem][j] != instance_of_split:
                    list_elements_in_a_row.append(original_matrix[elem][j])
            return_matrix.append(list_elements_in_a_row)
    else:
        list_of_indexs=[]
        for i in range(0,dim_row):
            for j in range(0,dim_column):
                if original_matrix[i][j] == instance_of_split and j == column_index:
                    list_of_indexs.append(i)
        return_matrix=[]
        for elem in list_of_indexs:
            list_elements_in_a_row=[]
            for j in range(0,dim_column):
                if original_matrix[elem][j] != instance_of_split and  j == column_index:
                    list_elements_in_a_row.append(original_matrix[elem][j])
            return_matrix.append(list_elements_in_a_row)
    return return_matrix

#to convert to a matrix a csv file, to better handle operations and access
def convert_csv_to_matrix(csvFile,dimRow,dimCol):
    return_matrix=[]
    for i in range(0,dimRow):
        list_elements_in_a_row=[]
        for j in range(0,dimCol):
            list_elements_in_a_row.append(csvFile.iloc[i,j])
        return_matrix.append(list_elements_in_a_row)
    return return_matrix

def return_ig(matrix,numberInstances,listcol,listwithlistinstances):
    myList=[]
    for i in range(0,len(listcol)):
        myList.append(information_gain(matrix,numberInstances,listcol[i],listwithlistinstances[i]))
    return myList

def byWhichCategorySplit(matrix,matrix_instances, numberOfTotalInstances,colNumbers):
    myReturnedIg=[]
    for i in range(len(matrix_instances)):
        myReturnedIg.append(information_gain(matrix,numberOfTotalInstances,colNumbers[i],matrix_instances[i]))
    return myReturnedIg


train_data_m = pd.read_csv("PlayTennis.csv") #importing the dataset from the disk


list_of_avalable_instances=["Sunny","Overcast","Rain"] # define all instances for the caracteristic
list_of_avalable_instances1=["Hot","Mild","Cool"] # define all instances for the caracteristic
list_of_avalable_instances3=["High","Normal"] # define all instances for the caracteristic
list_of_avalable_instances4=["Weak","Strong"] # define all instances for the caracteristic

matrix=convert_csv_to_matrix(train_data_m,14,5) #convert to matrix because it is more easy to work with


print(byWhichCategorySplit(matrix,[list_of_avalable_instances,list_of_avalable_instances1,list_of_avalable_instances3,list_of_avalable_instances4],14,[0 ,1,2,3]))

sunny_split=split_matrix_after_instance(matrix,14,5,"Sunny") #split the matrix
print(byWhichCategorySplit(sunny_split,[list_of_avalable_instances1,list_of_avalable_instances3,list_of_avalable_instances4],len(sunny_split),[0,1,2]))

sunny_humidity_split1 = split_matrix_after_instance(sunny_split,5,4,"High")
print(byWhichCategorySplit(sunny_humidity_split1,[list_of_avalable_instances3,list_of_avalable_instances4],len(sunny_humidity_split1),[0,1]))


sunny_humidity_split2 = split_matrix_after_instance(sunny_split,5,4,"Normal")
print(byWhichCategorySplit(sunny_humidity_split2,[list_of_avalable_instances3,list_of_avalable_instances4],len(sunny_humidity_split2),[0,1]))


overcast_split=split_matrix_after_instance(matrix,14,5,"Overcast") #split the matrix
print(byWhichCategorySplit(overcast_split,[list_of_avalable_instances1,list_of_avalable_instances3,list_of_avalable_instances4],len(overcast_split),[0,1,2]))


rain_split=split_matrix_after_instance(matrix,14,5,"Rain") #split the matrix
print(byWhichCategorySplit(rain_split,[list_of_avalable_instances1,list_of_avalable_instances3,list_of_avalable_instances4],len(rain_split),[0,1,2]))

rain_wind_split1 = split_matrix_after_instance(rain_split,5,4,"Weak")
print(byWhichCategorySplit(rain_wind_split1,[list_of_avalable_instances1,list_of_avalable_instances3],len(rain_wind_split1),[0,1]))
