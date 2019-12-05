This Repositry hosts a GUI-based application of the Weather Research and Forecasting Model (WRF) on a Raspberry Pi (version 3 or higher)


In order to run this application, the container platform, [Docker](https://www.docker.com/products/docker-desktop "Docker.com"), must be installed. If this OSX is the operating system being used, then the X server application, [XQuartz](https://www.xquartz.org/ "Xquartz") must be installed as well. If you are running the application on PC then you will need [VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/ "Windows X Server")


### Create a container & launch app (Raspberry Pi/Linux)
1. create container with "**docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw wefoust/pi-wrf**"
2. run app with the command "**run**"

### Create launch X11 Create a container and run app (Windows)
1. Open Xlaunch and use these settings:
  - page 1) multiple windows, Display number = -1
  - page 2) Start no client
  - page 3) Clipboard, Primary Selection, Native opengl, Disable Access Control
  - page 4) Finish
 
 2. Find Your IP Address
    1) Type network status in the search bar
    2) click ethernet (if connected via ethernet)
    3) click ethernet connected icon
    4) the IPv4 address is you IP address
 
 3. Run the app
    1) Open Windows command prompt
    2) type "**docker run -it --rm -e DISPLAY=YourIPaddress:0.0 wefoust/pi-wrf**"
    3) type "**run**" to run the application

### Create a container & launch app (MAC)
1. type the command "**open -a XQuartz**"
2. type the command "**IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')**"
3. type the command "**xhost + $IP**"
4. type "**docker run -it --rm -e DISPLAY=$IP:0 wefoust/pi-wrf**"
5. run the app with the command "**run**"


### Build from Source
This section is for users who have modified the WRF-Source Code. Make your changes to the source code and then run the following commands to build a new Docker Image. Warning: This may take a few hours to complete. 
1. CD into the top level directory
2. Build the image with the command "docker build -f envs/smpar_gui/dockerfile ."
