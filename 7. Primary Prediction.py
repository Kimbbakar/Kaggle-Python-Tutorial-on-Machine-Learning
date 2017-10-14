# Import the Numpy library
import pandas as pd
import numpy as np
# Import 'tree' from scikit-learn library
from sklearn import tree

# Load the train and test datasets to create two DataFrames 
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
 
 
# Convert the male and female groups to integer form
train.loc[train["Sex"] == "male",'Sex' ] = 0
train.loc[train["Sex"] == "female",'Sex' ] = 1


# Impute the Embarked variable
train["Embarked"] = train["Embarked"].fillna("S")


# Convert the Embarked classes to integer form
train.loc[ train["Embarked"]=='S', "Embarked" ] = 0
train.loc[ train["Embarked"]=='C', "Embarked" ] = 1
train.loc[ train["Embarked"]=='Q', "Embarked" ] = 2
  

# Print the train data to see the available features

train.Age =  train.Age.fillna( np.mean(train["Age" ]) ) 


# Create the target and features numpy arrays: target, features_one
target = np.array(train["Survived" ].values )
features_one = np.array((train[["Pclass", "Sex", "Age", "Fare"]].values))

 

# # Fit your first decision tree: my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one,target)

print(my_tree_one.feature_importances_)
print(my_tree_one.score(features_one, target))

# Convert the male and female groups to integer form
test.loc[test["Sex"] == "male",'Sex' ] = 0
test.loc[test["Sex"] == "female",'Sex' ] = 1

print(test.head())


test.Age =  test.Age.fillna(test.Age.mean() )
test.set_value(152,'Fare' ,test.Fare.median() )  

#alternate way to set value. test.Fare[152] =test.Fare.median()

