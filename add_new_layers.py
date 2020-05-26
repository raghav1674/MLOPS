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
