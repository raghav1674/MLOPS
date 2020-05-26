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

            
            os.system('curl --user "admin:redhat" 192.168.99.101:8080/job/train_and_tweak/build?token=retrain')
            
        elif count_ml >4:
            print("Can't be tweaked as per the threshold")
            os.system(f"echo 'Model can't be tweaked to the accuracy as per threshold' | mail -v -s 'MODEL TRAINED' raghav.81-cse-17@mietjammu.in")
            reset()
            exit()
        else:
            print("ACCURACY:",acc)
            reset(f2=False)
            acc=round(float(acc)*100,3)
            model=fie[0].split('_')[0]
            Dataset=fie[0].split('_')[1:]

        
            os.system(f"echo 'Model --> {model} Dataset ---> {Dataset}   Accuracy --> {acc}%' | mail -v -s 'MODEL TRAINED' raghav.81-cse-17@mietjammu.in")
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
            os.system('curl --user "admin:redhat" 192.168.99.101:8080/job/train_and_tweak/build?token=retrain')
        elif count_dl>4:
             
            os.system(f"echo 'Model can't be tweaked to the accuracy as per threshold' | mail -v -s 'MODEL TRAINED' raghav.81-cse-17@mietjammu.in")
            reset()
            exit()

        else:
            print("ACCURACY:",acc_dl)
            reset(f1=False)
            acc=round(float(acc_dl)*100,3)
            model=fie[0].split('_')[0]
            Dataset=fie[0].split('_')[1:]
        
            os.system(f"echo 'Model --> {model} Dataset ---> {Dataset}   Accuracy --> {acc}%' | mail -v -s 'MODEL TRAINED' raghav.81-cse-17@mietjammu.in")

