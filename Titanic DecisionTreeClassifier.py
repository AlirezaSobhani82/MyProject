import pandas
import numpy
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from pathlib import Path
#-----------------------------------------

#Add DataFrame
train_titanic = pandas.read_csv("D:\\Titanic train&test\\train titanic.csv")
pandas.set_option('display.max_columns', None)
#print(train_titanic)
test_titanic = pandas.read_csv("D:\\Titanic train&test\\test titanic.csv")
pandas.set_option('display.max_columns', None)
#print(test_titanic)

#Copy DataFrame train
train_titanic_1 = train_titanic.copy()

#List Split Unique Label Name
list_name = list(train_titanic_1["Name"])
#print(list_name)

split_name = []
for name in list_name:
    title = name.split(",")[1].split(".")[0].strip()
    split_name.append(title)
unique_name = numpy.unique(split_name)
#print(unique_name)

men = ["Mr","Major","Sir"]
boy = ["Master"]
women = ["Mrs","Mme","Lady"]
girl = ["Miss","Mlle","Ms"]
other = []
label_name = []
for name in split_name:
    if name in men:
        label_name.append(1)
    elif name in boy:
        label_name.append(2)
    elif name in women:
        label_name.append(3)
    elif name in girl:
        label_name.append(4)
    else:
        label_name.append(5)
#print(label_name)

#Add Column
train_titanic_1["name"] = label_name
#print(train_titanic_1)

#Delet Column
train_titanic_1 = train_titanic_1.drop(["Name"],axis=1)
#print(train_titanic_1)

#Index Column Sex
sex_type = ["male","female"]
train_titanic_1.Sex = train_titanic_1.Sex.apply(sex_type.index)
#print(train_titanic_1)

#Delet Column
train_titanic_1 = train_titanic_1.drop(["Ticket","Cabin"],axis=1)
#print(train_titanic_1)

#Get Dummies Embarked
get_dummies_embarked = pandas.get_dummies(train_titanic_1["Embarked"],dtype=int)
train_titanic_1 = train_titanic_1.join(get_dummies_embarked)
train_titanic_1 = train_titanic_1.drop(["Embarked"],axis=1)
#print(train_titanic_1)

#Train Test Split AccuracyScore
X = train_titanic_1.drop(["Survived"],axis=1).values
Y = train_titanic_1["Survived"].values
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,train_size=0.7,random_state=1)

#Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
trained_model = model.fit(xtrain,ytrain)
ypred = trained_model.predict(xtest)
accuracy_score_train = accuracy_score(ypred,ytest)
#print(accuracy_score_train)

#Change DateFrame TrainTitanic
#Copy DataFrame
test_titanic_1 = test_titanic.copy()
#print(test_titanic_1)

#List Split Unique Label Name
list_name_test = list(test_titanic_1["Name"])
#print(list_name)

split_name_test = []
for name in list_name_test:
    title = name.split(",")[1].split(".")[0].strip()
    split_name_test.append(title)
unique_name_test = numpy.unique(split_name_test)
#print(unique_name_test)

men_test = ["Mr","Major","Sir"]
boy_test = ["Master"]
women_test = ["Mrs","Mme","Lady"]
girl_test = ["Miss","Mlle","Ms"]
other_test = []
label_name_test = []
for name in split_name_test:
    if name in men_test:
        label_name_test.append(1)
    elif name in boy_test:
        label_name_test.append(2)
    elif name in women_test:
        label_name_test.append(3)
    elif name in girl_test:
        label_name_test.append(4)
    else:
        label_name_test.append(5)
#print(label_name_test)

#Add Column
test_titanic_1["name"] = label_name_test
#print(test_titanic_1)

#Delet Column
test_titanic_1 = test_titanic_1.drop(["Name"],axis=1)
#print(test_titanic_1)

#Index Column Sex
sex_type_test = ["male","female"]
test_titanic_1.Sex = test_titanic_1.Sex.apply(sex_type_test.index)
#print(test_titanic_1)

#Get Dummies Embarked
get_dummies_embarked_test = pandas.get_dummies(test_titanic_1["Embarked"],dtype=int)
test_titanic_1 = test_titanic_1.join(get_dummies_embarked_test)
test_titanic_1 = test_titanic_1.drop(["Embarked"],axis=1)
#print(test_titanic_1)

#Train Test Split AccuracyScore
X_test = test_titanic_1.drop(["Survived"],axis=1).values
Y_test = test_titanic_1["Survived"].values
ypred_test = trained_model.predict(X_test)
#print(ypred_test)
accuracy_score_test = accuracy_score(ypred_test,Y_test)
#print(accuracy_score_test)

#Add Label
test_titanic_2 = test_titanic.copy()
test_titanic_2["Predict Survived"] = ypred_test
#print(test_titanic_2)

#Path File
filepath = Path("D:\\Titanic train&test\\predict survived.csv")
filepath.parent.mkdir(parents=True,exist_ok=True)
test_titanic_2.to_csv(filepath)
