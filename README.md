This Repositry builds a Docker image for the GUI-based application of the Weather Research and Forecasting Model (WRF)
on a Raspberry Pi (version 3 or higher)


In order to build this application from source, the container platform, [Docker](https://www.docker.com "Docker.com")
must be installed. If this OSX is the operating system being used, then the X server application, [XQuartz](https://www.xquartz.org/ "Xquartz")
must be installed as well.


# Building the Docker Image
1. CD into the top level directory
2. Build the image with the command "docker build -f envs/smpar_gui/dockerfile ."


### Create a container & launch app (Linux)
1. create container with **"docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" id#"**
2. run app with the command **"run"**



### Create a container (MAC)
1. type the command **"open -a XQuartz"**
2. type the command **"IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')"**
3. type the command **"xhost + $IP"**
4. type **"docker run -it --rm -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix id#"**
5. run the app with the command **"run"**

