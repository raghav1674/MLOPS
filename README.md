

## MLOPS
### What is Automated Machine Learning?
Automated machine learning (AutoML) represents a fundamental shift in the way organizations of all 
sizes approach machine learning and data science. Applying traditional machine learning methods to 
real-world business problems is time-consuming, resource-intensive, and challenging. It requires experts
in the several disciplines, including data scientists – some of the most sought-after professionals in the job market right now.

Automated machine learning changes that, making it easier to build and use machine learning models in the real 
world by running systematic processes on raw data and selecting models that pull the most relevant information 
from the data – what is often referred to as “the signal in the noise.” Automated machine learning incorporates
machine learning best practices from top-ranked data scientists to make data science more accessible across the organization.


<img src="https://3gp10c1vpy442j63me73gy3s-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/Screen-Shot-2018-09-17-at-9.33.51-AM-e1537191346775-843x1024.png" height=500 width=400 align=center>


1.	Create container image that’s has Python3 and Keras or numpy installed using dockerfile 

##### SKLEARN ML DOCKERFILE (ON THE LEFT)                                                                   NN DOCKERFILE (ON  THE RIGHT)
<img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dockerfile%20ml.PNG" alt="mldockerfile" height=300 width=400><img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dldockerfile.PNG" height=300 width=400 align=right>


![REQUIREMENTSFILE](https://github.com/raghav1674/MLOPS/blob/master/ml.txt)


### Job1 : Pull the Github repo automatically when some developers push repo to Github.


        
<img src="https://3gp10c1vpy442j63me73gy3s-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/Screen-Shot-2018-09-17-at-9.33.51-AM-e1537191346775-843x1024.png" height=500 width=400 align=center>





### JOB2 :When we launch this image, it should automatically starts train the model in the container.
      
 By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed       interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
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










#### 5. Send the Mail 


      






#### 6.Create One extra job: for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left






