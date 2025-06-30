import pandas
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
#-----------------------------------------

#Add DataFrame
train_titanic = pandas.read_csv("D:\\Titanic train&test\\train titanic.csv")
pandas.set_option('display.max_columns', None)
#print(train_titanic)

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

#Column Age
lambda_Age = lambda x: x.fillna(x.mean())
label_age = list(train_titanic_1.groupby("name")["Age"].transform(lambda_Age))

#Add Column
train_titanic_1["age"] = label_age

#Delet Column
train_titanic_1 = train_titanic_1.drop("Age",axis=1)

#Train Test Split AccuracyScore
X = train_titanic_1.drop(["Survived"],axis=1).values
Y = train_titanic_1["Survived"].values
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,train_size=0.7,random_state=1)

#Scaler
scaler = StandardScaler()
scaler.fit(xtrain)
Xtrain = scaler.transform(xtrain)
Xtest = scaler.transform(xtest)

#KNN
model = KNeighborsClassifier(n_neighbors=6)
trained_model = model.fit(Xtrain,ytrain)
ypred = trained_model.predict(Xtest)

#Accuracy Score
accuracy_score_train = accuracy_score(ypred,ytest)
#print(accuracy_score_train)

##Plt Accuracy
test_score = []
train_score = []
list_range = list(range(1,21))
for num in list_range:
    model = KNeighborsClassifier(n_neighbors=num,metric="minkowski")
    trained_model = model.fit(Xtrain,ytrain)
    test_score.append(trained_model.score(Xtest,ytest))
    train_score.append(trained_model.score(Xtrain,ytrain))
plt.plot(list_range,train_score,label="Train")
plt.plot(list_range,test_score,label="Test")
plt.legend()
plt.xlabel("Number Of Neighbors")
plt.ylabel("Accuracy Score")
#plt.show()

print(max(test_score))
print(len(test_score))
print(test_score.index(max(test_score)))
