This Repositry hosts a GUI-based application of the Weather Research and Forecasting Model (WRF) on a Raspberry Pi (version 3 or higher)


In order to run this application, the container platform, [Docker](https://www.docker.com/products/docker-desktop "Docker.com"), must be installed. If this OSX is the operating system being used, then the X server application, [XQuartz](https://www.xquartz.org/ "Xquartz") must be installed as well.


### Create a container & launch app (Raspberry Pi/Linux)
1. create container with **"docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" docker pull wefoust/pi-wrf:3.9.1-SMPAR-gui"**
2. run app with the command **"run"**



### Create a container & launch app (MAC)
1. type the command **"open -a XQuartz"**
2. type the command **"IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')"**
3. type the command **"xhost + $IP"**
4. type **"docker run -it --rm -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix wefoust/pi-wrf:3.9.1-SMPAR-gui"**
5. run the app with the command **"run"**


### Build from Source
This section is for users who have modified the WRF-Source Code. Make your changes to the source code and then run the following commands to build a new Docker Image. Warning: This may take a few hours to complete. 
1. CD into the top level directory
2. Build the image with the command "docker build -f envs/smpar_gui/dockerfile ."
