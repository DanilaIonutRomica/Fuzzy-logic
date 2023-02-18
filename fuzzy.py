
def Fuzzification(data_matrix, list_of_matrix_names_and_range_of_fuzzy_caracters_per_column):
    """This function is used to convert real-valued numbers into fuzzy values.:[number] -> [string fuzzy value], if the number is between the values for that string's fuzzy value.

        Parameters
        ----------
        data_matrix : matrix
            This parameter is used to store the real values, which will be transformed into fuzzy values.
        
        list_of_matrix_names_and_range_of_fuzzy_caracters_per_col : list of matrices
            This parameter is used to store a list of matrices that will be used for each column; each matrix shall have the fuzzy values and two real values that will act as a bound for the real value.

        Returns
        -------
        matrix
            a the matrix with the fuzzy values
        """
    data_matrix=list(zip(*data_matrix)) #transpose of the matrix for easy work with columns
    rez_column_matrix=[]
    for i in range(0,len(data_matrix)):
        fuzzy_caracteristics=list_of_matrix_names_and_range_of_fuzzy_caracters_per_column[i]
        column=[]
        for element in data_matrix[i]:
            for j in range(0,len(fuzzy_caracteristics[0])):
                if type(element) == str:
                    pass
                else:
                    if element >= fuzzy_caracteristics[1][j] and element <= fuzzy_caracteristics[2][j]:
                        element=fuzzy_caracteristics[0][j]
                        column.append(element) #TODO: See if it is necessary to make a new matrix, if not, return data_matrix.
        rez_column_matrix.append(column)
    
    return list(zip(*rez_column_matrix))


matrix=[[1.2, 1.4, 15], [5.2 ,25,6], [5.5,5,2] ]
list_matrix=[
    [
        ['fuzzy_val_11', "fuzzy_val_12", "fuzzy_val_13"], [0,2.11,5.4], [2.1,5.3,10000]  #matrix for the first column in the data matrix: if an element from the first column is between 0 and 2.1, the element will have the fuzzy value 11.
    ],
    [
        ['fuzzy_val_21', "fuzzy_val_22", "fuzzy_val_23"], [0,100,1000], [100,1000,10000]
    ],
    [
        ['fuzzy_val_31', "fuzzy_val_32", "fuzzy_val_33"], [0,100,1000], [100,1000,10000]
    ]
]

print(Fuzzification(matrix,list_matrix))
matrix=Fuzzification(matrix,list_matrix)

