import pandas
import numpy
import seaborn as sns
import matplotlib.pyplot as plt
#------------------------------


#add file excel
data_frame_1 = pandas.read_csv("D:\\Titanic Pro\\train titanic.csv")
pandas.set_option('display.max_columns', None)
#print(data_frame_1)

#split name
#str_name = "Braund, Mr. Owen Harris"
#print(str_name.split(",")[1].split(".")[0].strip())
name_list = list(data_frame_1["Name"])
title_split = []
for name in name_list:
    title = name.split(",")[1].split(".")[0].strip()
    title_split.append(title)
#print(title_split)

#unique name
unique_name = []
for unique in title_split:
    if unique not in unique_name:
        unique_name.append(unique)
#print(unique_name)

#label for name
men = ["Mr","Major","Sir"]
boy = ["Master"]
women = ["Mrs","Mme","Lady"]
girl = ["Miss","Mlle","Ms"]
other = []
labels_name = []
for label in title_split:
    if label in men:
        labels_name.append(1)
    elif label in boy:
        labels_name.append(2)
    elif label in women:
        labels_name.append(3)
    elif label in girl:
        labels_name.append(4)
    else:
        labels_name.append(5)
#print(labels_name)

#Add Column
data_frame_1["Name Label"] = labels_name
#print(data_frame_1)

#Copy DataFrame
data_frame_2 = data_frame_1.copy()
#print(data_frame_2)

#Delet Column
data_frame_2 = data_frame_2.drop(["Name","Ticket","Cabin"],axis=1)
#print(data_frame_2)

#unique sex
sex_list = list(data_frame_2["Sex"])
unique_sex = numpy.unique(sex_list)
#print(unique_sex)

#label for sex
labels_sex = []
for sex in sex_list:
    if sex == "female":
        labels_sex.append(1)
    elif sex == "male":
        labels_sex.append(0)
#print(labels_sex)

#Add Column
data_frame_2["Sex Label"] = labels_sex
#print(data_frame_2)

#Delet Column
data_frame_2 = data_frame_2.drop("Sex",axis=1)
#print(data_frame_2)

#unique embarked
embarked_list = list(data_frame_2["Embarked"])
unique_embarked = numpy.unique(embarked_list)
#print(unique_embarked)

#label for embarked
labels_embarked = []
for embarked in embarked_list:
    if embarked == "C":
        labels_embarked.append(1)
    elif embarked == "Q":
        labels_embarked.append(2)
    elif embarked == "S":
        labels_embarked.append(3)
    else:
        labels_embarked.append(0)
#print(labels_embarked)

#Add Column
data_frame_2["Embarked Label"] = labels_embarked
#print(data_frame_2)

#Delet Column
data_frame_2 = data_frame_2.drop("Embarked",axis=1)
#print(data_frame_2)

#NaN
#print(data_frame_2.isna().sum())

#mean age
lambda_mean = lambda x: x.fillna(x.mean())
#print(data_frame_2.groupby("Name Label").mean().Age)
#print(data_frame_2.groupby(["Name Label"])["Age"].transform(lambda_mean))

#Add Column
age_list = list(data_frame_2.groupby(["Name Label"])["Age"].transform(lambda_mean))
data_frame_2["Age Label"] = age_list
#print(data_frame_2)

#Delet Column
data_frame_2 = data_frame_2.drop("Age",axis=1)
#print(data_frame_2)

#Copy DataFrame
data_frame_3 = data_frame_1.copy()

#cross
crosstab_1 = pandas.crosstab(data_frame_3["Name Label"], data_frame_3["Survived"])
#print(crosstab_1)

#div crosstab
div_crosstab_1 = crosstab_1.div(crosstab_1.sum(1),axis=0)
#print(div_crosstab_1)

#cross
crosstab_2 = pandas.crosstab(data_frame_3["Name Label"],[data_frame_3["Sex"],data_frame_3["Survived"]])
#print(crosstab_2)

#barchart
plt.close("all")
div_crosstab_1.plot(kind="bar",stacked=True,title="Survived Rate")
plt.figure()
#plt.show()

#Delet Column
data_frame_4 = data_frame_3.drop(["Name","Ticket","Cabin","PassengerId"],axis=1)
#print(data_frame_4)

#get dummies
get_dummies_1 = pandas.get_dummies(data_frame_4["Embarked"],dtype="int")
#print(get_dummies_1)

#Delet Column
data_frame_4 = data_frame_4.drop(["Embarked"],axis=1)
#print(data_frame_4)

#Add Column
data_frame_4 = data_frame_4.join(get_dummies_1)
#print(data_frame_4)

#seaborn
plt.close("all")
sns.catplot(x="Sex",hue="Survived",data=data_frame_4,kind="count")
plt.figure()
#plt.show()

#groupby
groupby_1 = data_frame_4.groupby(["Survived","Pclass"])
#print(groupby_1.size())

#heat map
plt.close("all")
heat = groupby_1.size().unstack()
sns.heatmap(heat,annot=True,fmt="d")
plt.figure()
#plt.show()

#women & men
women_1 = data_frame_4[data_frame_4["Sex"]=="female"]
men_1 = data_frame_4[data_frame_4["Sex"]=="male"]
#print(women_1["Age"].mean())
#print(men_1["Age"].mean())

#plot women & men
plt.close("all")
women_1["Age"].plot(kind="hist",label="Women")
plt.legend()
plt.figure()
#plt.show()

plt.close("all")
men_1["Age"].plot(kind="hist",label="Men")
plt.legend()
plt.figure()
#plt.show()

#Free
#print(len(data_frame_4[data_frame_4["Fare"]<1]))
#print(data_frame_4[data_frame_4["Fare"]<1])

#cat plot
plt.close("all")
sns.catplot(x="Survived",hue="Embarked",data=data_frame_1,kind="count")
plt.figure()
#plt.show()

plt.close("all")
sns.catplot(x="Survived",col="Embarked",data=data_frame_1,kind="count")
plt.figure()
#plt.show()

plt.close("all")
sns.catplot(x="Survived",col="Sex",hue="Pclass",data=data_frame_1,kind="count")
plt.figure()
#plt.show()

#box
plt.close("all")
sns.boxenplot(x="Pclass",y="Age",data=data_frame_1)
plt.figure()
#plt.show()
