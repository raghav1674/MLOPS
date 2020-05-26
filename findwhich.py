
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

