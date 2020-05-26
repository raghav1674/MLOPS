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
    
