import numpy
import pandas
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#----------------------------------------------------


#Add Data Set
iris = datasets.load_iris()
pandas.set_option('display.max_columns', None)
#print(iris)


#X & Y
X = iris.data[:,0:2]
Y = iris.target
#print(X)
#print(Y)


#Train Test
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,train_size=0.8,random_state=1)


#SVM
classifier_model = svm.SVC()
trained_model = classifier_model.fit(xtrain,ytrain)
ypredict = trained_model.predict(xtest)
accuracy_score_model = accuracy_score(ypredict,ytest)
#print(accuracy_score_model)


#Model
model_1 = svm.SVC(kernel="linear",C=1)
model_2 = svm.LinearSVC(C=1)
model = (model_1,model_2)
trained_fit = (i.fit(xtrain,ytrain) for i in model)
#print(list(trained_fit))


#Make Meshgrid
def meke_mesh(x,y,resolution=0.02):
    x_min = x.min()-1
    x_max = x.max()+1
    y_min = y.min()-1
    y_max = y.max()+1
    range_x = numpy.arange(x_min,x_max,resolution)
    range_y = numpy.arange(y_min,y_max,resolution)
    mesh_x , mesh_y = numpy.meshgrid(range_x, range_y)
    return mesh_x , mesh_y


#Make Ravel
def make_ravel(ax,clf,mesh_x,mesh_y,**params):
    class_predict = clf.predict(numpy.c_[mesh_x.ravel(),mesh_y.ravel()])
    class_predict = class_predict.reshape(mesh_x.shape)
    plt_contourf = ax.contourf(mesh_x,mesh_y,class_predict,**params)
    return plt_contourf


#Subplots
fig,sub = plt.subplots(1,2)
plt.subplots_adjust(wspace=0.5,hspace=0.5)
#plt.show()


titles = ("Linear Kernel","Linear SVC")
mesh_x,mesh_y = meke_mesh(X[:,0],X[:,1])


#Plot
for cl,title,ax in zip(trained_fit,titles,sub.flatten()):
    make_ravel(ax,cl,mesh_x,mesh_y,cmap=plt.cm.coolwarm,alpha=0.7)
    ax.scatter(X[:,0],X[:,1],c=Y,cmap=plt.cm.coolwarm,s=30,edgecolors='k')
    ax.set_xlim(mesh_x.min(),mesh_x.max())
    ax.set_ylim(mesh_y.min(),mesh_y.max())
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    ax.set_title(title)
plt.show()
