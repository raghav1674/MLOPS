
FROM centos
RUN mkdir /my_mlws
WORKDIR my_mlws
COPY ./ml.txt /my_mlws/requirements.txt
RUN yum install python3 -y
RUN yum install net-tools -y
RUN yum install coreutils --allowerasing -y
                                    #for pwd to change the directory and getcwd
RUN yum install sudo -y
RUN yum install openssh-clients -y
RUN pip3 install -r requirements.txt
CMD python3 


 
