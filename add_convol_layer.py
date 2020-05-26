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


