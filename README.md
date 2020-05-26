

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


<img src="https://3gp10c1vpy442j63me73gy3s-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/Screen-Shot-2018-09-17-at-9.33.51-AM-e1537191346775-843x1024.png" height=500 width=400,align=center>


1.	Create container image that’s has Python3 and Keras or numpy installed using dockerfile 

##### SKLEARN ML DOCKERFILE (ON THE LEFT)                                                                   NN DOCKERFILE (ON  THE RIGHT)
<img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dockerfile%20ml.PNG" alt="mldockerfile" height=300 width=400><img src="https://github.com/raghav1674/MLOPS/blob/master/mlops%20great/dldockerfile.PNG" height=300 width=400 align=right>


![REQUIREMENTSFILE](https://github.com/raghav1674/MLOPS/blob/master/ml.txt)


### Job1 : Pull the Github repo automatically when some developers push repo to Github.


        
<img src="https://3gp10c1vpy442j63me73gy3s-wpengine.netdna-ssl.com/wp-content/uploads/2018/03/Screen-Shot-2018-09-17-at-9.33.51-AM-e1537191346775-843x1024.png" height=500 width=400,align=center>





### JOB2 :When we launch this image, it should automatically starts train the model in the container.
      
 By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed       interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
 ## JOB3:Train your model and predict accuracy or metrics.

## Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture.   
      
#### 1.FEATURE SCALING:
      
  Feature scaling is a method used to normalize the range of independent variables or features of data. In data processing, it is         also known as data normalization and is generally performed during the data preprocessing step.



#### 2. ADDING DENSE LAYERS AND SETTING THE NUMBERS OF NEURONS (we can also alter the number of epochs):
      
  Dense layer is the regular deeply connected neural network layer. It is most common and frequently used layer. Dense layer does         the below operation on the input and return the output. output = activation(dot(input, kernel) + bias)

#### 3. ADDING THE CONVOLUTION LAYERS , SETTING TH NUMBER OF FILTERS, FILTER SIZE AND STRIDE RATE:
      

  <img src="https://miro.medium.com/max/654/1*hy15RJHCqT4HzO2VUydjTw.png" height=500 , weight=300>
       
       
       
       
       










#### 4.Retrain the model or notify that the best model is being created










#### 5. Send the Mail 


      






#### 6.Create One extra job: for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left






