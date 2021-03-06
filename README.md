

# MLOPS
### What is Automated Machine Learning?
Automated machine learning (AutoML) represents a fundamental shift in the way organizations of all 
sizes approach machine learning and data science. Applying traditional machine learning methods to 
real-world business problems is time-consuming, resource-intensive, and challenging. It requires experts
in the several disciplines, including data scientists – some of the most sought-after professionals in the job market right now.

Automated machine learning changes that, making it easier to build and use machine learning models in the real 
world by running systematic processes on raw data and selecting models that pull the most relevant information 
from the data – what is often referred to as “the signal in the noise.” Automated machine learning incorporates
machine learning best practices from top-ranked data scientists to make data science more accessible across the organization.

##### HYPER PARAMETERS:
 
 What is a hyperparameter?

A hyperparameter is a parameter that is set before the learning process begins. These parameters are tunable and can directly affect how well a model trains. Some examples of hyperparameters in machine learning:

1.Learning Rate


2.Number of Epochs

3.Momentum

4.Regularization constant


5.Number of branches in a decision tree


6.Number of clusters in a clustering algorithm (like k-means)




### Optimizing Hyperparameters

##### Hyperparameters can have a direct impact on the training of machine learning algorithms. Thus, in order to achieve maximal performance, it is important to understand how to optimize them. Here are some common strategies for optimizing hyperparameters:

##### Grid Search: Search a set of manually predefined hyperparameters for the best performing hyperparameter. Use that value. (This is the traditional method)

##### Random Search: Similar to grid search, but replaces the exhaustive search with random search. This can outperform grid search when only a small number of hyperparameters are needed to actually optimize the algorithm.

##### Bayesian Optimization: Builds a probabilistic model of the function mapping from hyperparameter values to the target evaluated on a validation set. 

##### Gradient-Based Optimization: Compute gradient using hyperparameters and then optimize hyperparameters using gradient descent.

### Evolutionary Optimization

: Uses evolutionary algorithms (e.g. genetic functions) to search the space of possible hyperparameters. 

<img src="https://3gp10c1vpy442j63me73gy3s-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/Screen-Shot-2018-09-17-at-9.33.51-AM-e1537191346775-843x1024.png" height=700 width=600 align=center>


#### 1.	Create container image that’s has Python3 and Keras or numpy installed using dockerfile 

##### SKLEARN ML DOCKERFILE (ON THE LEFT)                                                                   NN DOCKERFILE (ON  THE RIGHT)
<img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dockerfile%20ml.PNG" alt="mldockerfile" height=300 width=400><img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dldockerfile.PNG" height=300 width=400 align=right>


![REQUIREMENTSFILE](https://github.com/raghav1674/MLOPS/blob/master/ml.txt)


### Job1 : Pull the Github repo automatically when some developers push repo to Github.


        
<img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/github.PNG" height=300 width=600 align=center>





### JOB2 :When we launch this image, it should automatically starts train the model in the container.
      
 By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed       interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).
      
 ```python
  import sys
import os
import json
def write_to(filename,types):
    os.system("touch /root/MLOPsProject/all_storage/"+types+"_"+filename)
    d={}
    with open("all_storage/"+types+"_"+filename,'w') as f:
        d["filename"]=filename
        d["type"]=types
        f.write(json.dumps(d))
def which_file():

    os.system("rm -rf /traditional_ml")
    os.system("mkdir /traditional_ml")

    os.system("rm -rf /cnn_dl")
    os.system("mkdir /cnn_dl")
    path=sys.argv[1]
    
    if os.path.exists(path):
    
        assert path is not None and path != "","Please provide the path of the directory or file"
        files=[]
        isFile=False
        if os.path.isfile(path):
            files.append(path)
            isFile=True

        else:
            files = os.listdir(path)
        try:
            for filename in files:
                ext = str(os.path.splitext(filename)[1])

                # if ext.lower() in [".jpeg", ".dat", ".png", ".h5", ".jpg", ".db", ".csv",".mp4",".wav",".mp3",".vdi",".exe",".xlsx",".log"," "]:
                    # print("Can't read", filename)
                if ext.lower() == ".py":
                    if isFile:
                        
                        filename=filename
                    else:
                        filename = os.path.join(path, filename)
                    with open(filename, "r") as fp:
                        lines = fp.readlines()
                        for line in lines:
                            line=line.lower()
                            
                            if "sklearn" in line:
                                if ("logisticregression" in line):
                                    write_to(os.path.basename(filename),"LogisticRegression")
                        
                                    print(filename,": LogisticRegression")
                                    os.system("cp {0} /traditional_ml".format(filename))
                                elif ("linearregression" in line):
                                    
                                    write_to(os.path.basename(filename),"LinearRegression")
                                    print(filename,": LinearRegression")
                                    
                                    os.system("cp {0} /traditional_ml".format(filename))
                                elif "kneighbors" in line:
                                    
                                    write_to(os.path.basename(filename),"KNN")
                                    os.system("cp {0} /traditional_ml".format(filename))
                                    print(filename,": KNN")
                                elif "kmeans" in line:
                                    
                                    write_to(os.path.basename(filename),"KMeans")
                                    os.system("cp {0} /traditional_ml".format(filename))
                                    print(filename,": UNSUPERVISED KMEANS")
                                    break

                            if "keras" in line or ("vgg16" in line or "resnet50" in line or "inception" in line or "mobilenet" in line ):
                                
                                if "vgg16" in line:
                                    
                                    write_to(os.path.basename(filename),"VGG16")
                                    os.system("cp {0} /cnn_dl".format(filename))
                                    print(filename,": VGG16")
                                    break
                                elif "resnet50" in line:
                                    
                                    write_to(os.path.basename(filename),"Resnet50")
                                    os.system("cp {0} /cnn_dl".format(filename))
                                    print(filename,": Resnet50")
                                    break
                                elif "inception" in line:
                                    
                                    write_to(os.path.basename(filename),"INCEPTION")
                                    os.system("cp {0} /cnn_dl".format(filename))
                                    print(filename,": Inception")
                                    break
                                elif "mobilenet" in line:
                                   
                                    write_to(os.path.basename(filename),"MobileNet")
                                    os.system("cp {0} /cnn_dl".format(filename))
                                    print(filename,": Mobilenet")
                                    break

                                elif  "dense" in line:
                                    
                                    write_to(os.path.basename(filename),"ANN")

                                    os.system("cp {0} /cnn_dl".format(filename))

                                    print(filename,": ANN")
                                    break
                                elif "convolution2d" in line or "conv2d" in line  :
                                    
                                    write_to(os.path.basename(filename),"CNN")
                                    os.system("cp {0} /cnn_dl".format(filename))
                                    print(filename,": CNN")
                                    break
                else:
                            
                    filename = os.path.join(path, filename)
            
                    os.system("cp -rf  {0} /traditional_ml/".format(filename))
                    os.system("cp -rf  {0} /cnn_dl/".format(filename))                
        except Exception as e:
            print(e)
            #print(path, "cannot be accessed")
    else:
        print(path,"doesn't exists")


which_file()
    
      
  ```     
      
## JOB3:Train your model and predict accuracy or metrics.

## Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture.   
      
#### 1.FEATURE SCALING:
      
  Feature scaling is a method used to normalize the range of independent variables or features of data. In data processing, it is         also known as data normalization and is generally performed during the data preprocessing step.


  
```python
toscale='from sklearn.preprocessing import StandardScaler\nsc=StandardScaler()\nX_train=sc.fit_transform(X_train)'

X_test="X_test=sc.transform(X_test)"
import sys
from fileinput import *
files=sys.argv[1]
scaled=False
with FileInput(files) as f:
    for line in f:
        if "Standard" in line:
            scaled=True
            break
        else:
            continue

if scaled ==False:
    with FileInput(files,inplace=True) as f:
        for line in f:
            #if "X_train,X_test,y_train,y_test=train_test_split"  in line:
            if "X_train,X_test,y_train,y_test=train_test_split" in line:
                print(line.replace(line,line.strip()+"\n"+toscale.strip()))

            if "model.fit" in  line:
                print(line.replace(line,line.strip()+"\n"+X_test.strip()))
            else:
               if "X_train,X_test,y_train,y_test=train_test_split" not in line:
                print(line.strip())
  
 ```



#### 2. ADDING DENSE LAYERS AND SETTING THE NUMBERS OF NEURONS (we can also alter the number of epochs):
      
  Dense layer is the regular deeply connected neural network layer. It is most common and frequently used layer. Dense layer does         the below operation on the input and return the output. output = activation(dot(input, kernel) + bias)
```python
import random
def add_layers(n,units):
    units=random.randint(n*units,n*units+units)
    activ="+acti+"
    layer=n*"model.add(Dense(units={0},activation='relu'))\n".format(units)
  
    return layer
X_test="X_test=sc.transform(X_test)"
import sys
from fileinput import *
files=sys.argv[1]
count=0
with FileInput(files) as f:
    for line in f:
        if "model.add(Dense" in line:
            count=count+1
            
        else:
            continue

if count < 4:
    if count==0:
        n=4
    else:
    	n=4-count
    with FileInput(files,inplace=True) as f:
        for line in f:
            if "model.add(Dense" in line and "input_shape" in line:
                lineadd=add_layers(n,20) 
                print(line.replace(line,line+"\n"+lineadd.strip()))
            else:
               print(line.strip())



```

#### 3. ADDING THE CONVOLUTION LAYERS , SETTING THE NUMBER OF FILTERS, FILTER SIZE AND STRIDE RATE:
      

  <img src="https://miro.medium.com/max/654/1*hy15RJHCqT4HzO2VUydjTw.png" height=500  weight=300>
  
  ```python
  import random
def add_Convlayers(n,filters,filter_size=(3,3),strides=(2,2)):
    filters=random.randint(n*units,n*units+units)
    
    layer=n*"model.add(Convolution2D(filters={0},filter_size={1},strides={3},activation='relu'))\nmodel.add(MaxPolling2D(pool_size=(2,2)))\n".format(filters,filter_size,strides)
  
    return layer
X_test="X_test=sc.transform(X_test)"
import sys
from fileinput import *
files=sys.argv[1]
count=0
with FileInput(files) as f:
    for line in f:
        if "model.add(Conv" in line:
            count=count+1
            
        else:
            continue

if count < 4:
    if count==0:
        n=4
    else:
    	n=4-count
    with FileInput(files,inplace=True) as f:
        for line in f:
            if "model.add(Convo" in line and "input_shape" in line:
                lineadd=add_Convlayers(n,50) 
                print(line.replace(line,line+"\n"+lineadd.strip()))
            else:
               print(line.strip())

  
  
  
  ```
  
  
       
       
       
       
#### 4.Retrain the model or notify that the best model is being created


```python
def get_var_value(filename="/root/MLOPsProject/varstore.dat"):
    with open(filename, "r+") as f:
        f.seek(0)
        val = int(f.read()) + 1
        f.seek(0)
    
        f.write(str(val))
        return val
def get_var_value_ml(filename="/root/MLOPsProject/varstore_ml.dat"):
    with open(filename, "r+") as f:
        f.seek(0)
        val = int(f.read()) + 1
        f.seek(0)
        
        f.write(str(val))
        return val
def reset(file1="/root/MLOPsProject/varstore_ml.dat",file2="/root/MLOPsProject/varstore.dat",f1=True,f2=True):
    if f1:
        with open(file1,"w+") as f:
            f.seek(0)
            f.write(str(0))
    if f2:
        with open(file2,"w+") as f:
            f.seek(0)
            f.write(str(0))



import os
import subprocess
import sys
which_container=sys.argv[1]
threshold=0.8

count_ml,count_dl=0,0
acc_ml=[]
acc=[]
curr_files=[]
fie=[]
#workdir=sys.argv[2]
#mount_storage=sys.argv[3]
if which_container=="sklearn_ml":
    workdir="/my_mlws/"
    mount_storage="/traditional_ml/"
elif which_container=="cnn_dl":
    workdir="/my_dlws/"
    mount_storage="/cnn_dl/"
files=os.listdir(mount_storage)
files=[file for file in files if os.path.splitext(file)[1] !=".csv"]
for file in files:
    if os.path.splitext(file)[1] == ".py":
        print(file)
        curr_files.append(file)
        base=os.path.splitext(file)[0]
        files.remove(file)
        for fi in files:
            print(fi)
            if base in fi:
                fie.append(fi)
                print(fi,file,which_container)
        
                
                cmd='sudo docker exec {0} bash -c "cd {1}; python3 {2} > {3}"'.format(which_container,workdir,file,fi)
                print(cmd)
                os.system(cmd)
                
if which_container =="sklearn_ml":                
    with open("/traditional_ml/"+fie[0]) as fp:
        accuracy=fp.read()
        acc_ml.append(round(float(accuracy.strip()),4))
        acc=acc_ml.pop()
        if acc < threshold:
            print(acc)
            count_ml=get_var_value_ml()
            if count_ml <= 2:
                os.system("python3 /root/MLOPsProject/add_new_layers.py"+" "+"/traditional_ml/"+curr_files[0]) 
            elif count_ml > 3 and count_ml <= 5: 
                os.system("python3 /usr/bin/featureScaling.py"+" "+"/traditional_ml/"+curr_files[0])

            
            os.system('curl --user "admin:redhat" IP:8080/job/train_and_tweak/build?token=retrain')
            
        elif count_ml >4:
            print("Can't be tweaked as per the threshold")
            os.system(f"echo 'Model can't be tweaked to the accuracy as per threshold' | mail -v -s 'MODEL TRAINED' emailid")
            reset()
            exit()
        else:
            print("ACCURACY:",acc)
            reset(f2=False)
            acc=round(float(acc)*100,3)
            model=fie[0].split('_')[0]
            Dataset=fie[0].split('_')[1:]

        
            os.system(f"echo 'Model --> {model} Dataset ---> {Dataset}   Accuracy --> {acc}%' | mail -v -s 'MODEL TRAINED' emailid")
elif which_container =="cnn_dl":  
    with open("/cnn_dl/"+fie[0]) as fp:
        accuracy=fp.readlines()[-1]
        acc.append(round(float(accuracy.strip()),4))
        acc_dl=acc.pop()
        if acc_dl < threshold:

            count_dl=get_var_value()
            print(acc_dl)
            if count_dl<= 2:
                print("add")
                os.system("python3 /root/MLOPsProject/add_new_layers.py"+" "+"/cnn_dl/"+curr_files[0])
            elif count_dl >= 4 or count_dl <= 5:
                print("fs")
                os.system("python3 /usr/bin/featureScaling.py"+" "+"/cnn_dl/"+curr_files[0])
            
        
            print(count_dl)
            os.system('curl --user "admin:redhat" ip:8080/job/train_and_tweak/build?token=retrain')
        elif count_dl>4:
             
            os.system(f"echo 'Model can't be tweaked to the accuracy as per threshold' | mail -v -s 'MODEL TRAINED' emailid")
            reset()
            exit()

        else:
            print("ACCURACY:",acc_dl)
            reset(f1=False)
            acc=round(float(acc_dl)*100,3)
            model=fie[0].split('_')[0]
            Dataset=fie[0].split('_')[1:]
        
            os.system(f"echo 'Model --> {model} Dataset ---> {Dataset}   Accuracy --> {acc}%' | mail -v -s 'MODEL TRAINED' emailid")




```



<img src="https://github.com/raghav1674/MLOPS/blob/master/WhatsApp%20Image%202020-05-26%20at%204.06.02%20PM.jpeg" width=300 height=600><img src="https://github.com/raghav1674/MLOPS/blob/master/WhatsApp%20Image%202020-05-26%20at%204.06.02%20PM%20(2).jpeg" width=300 height=600 align=right> 
#### Create One extra job: for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left

<img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/build%20pipeline.PNG" height=400 width=900>




