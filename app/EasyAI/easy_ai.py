import numpy as np
from sklearn.model_selection import train_test_split
from app.EasyAI import easy_ai_regression
from app.EasyAI import easy_ai_classification



'''To anyone reading this: Yes I know this code would be much shorter by just
looping over all the classifiers and their hyperparameters from an array or something
but this is vastly more readable as a first draft
'''




def convert_to_sklearn_shape(x):
    converted_data = []
    for index in range(len(x[0])):
        row = []
        for feature in x:
            row.append(feature[index])
        converted_data.append(row)
    return converted_data

#In order to normalize data, each feature must be turned into its own column
#rather than having observations of each feature and a label as a column
#so that statistics like the mean and standard deviation can be calculated
def convert_to_analysis_shape(x):
    converted_data = []
    for entry in x[0]:
        converted_data.append([entry])
    for index in range(1,len(x)):
        for col_index in range(len(x[index])):
            converted_data[col_index].append(x[index][col_index])
    
    return converted_data

#Assumes features follow a normal distribution and converts them to z scores
#Will be looking into different methods of normalization that don't assume
#normal distribution. Perhaps dividing by L2 Norm?
def data_norm(x):
    for feature in x:
        mean = np.mean(feature)
        stdev = np.std(feature)
        feature = (feature - mean) / stdev
        
    return x

def easyanalysis(input_filename, datatype):
    input_array = np.genfromtxt('C:/Users/Matt/Documents/graymatter-flask/assets/tempdata/'+input_filename, delimiter = ',', skip_header = 1)
    x = []
    y = []
    for row in input_array:
        y.append(row[-1])
        x.append(row[:-1])
        
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
    analysis_shape_x_train = convert_to_analysis_shape(x_train)
    analysis_shape_normed_x_train = data_norm(analysis_shape_x_train)
    analysis_shape_x_test = convert_to_analysis_shape(x_test)
    analysis_shape_normed_x_test = data_norm(analysis_shape_x_test)
    
    
    
    sk_learn_compatible_normed_x_train = convert_to_sklearn_shape(analysis_shape_normed_x_train)
    sk_learn_compatible_normed_x_test = convert_to_sklearn_shape(analysis_shape_normed_x_test)
    
    label_type = datatype
    
    if label_type.lower() == "classification":
        return easy_ai_classification.easy_classification(input_filename, sk_learn_compatible_normed_x_train, y_train, sk_learn_compatible_normed_x_test, y_test)
    elif label_type.lower() == "regression":
        return easy_ai_regression.easy_regression(input_filename, sk_learn_compatible_normed_x_train, y_train, sk_learn_compatible_normed_x_test, y_test)
            
