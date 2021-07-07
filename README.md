# kivy-xtide
An implimentation of xtide using Kivy. 

## Description
The goal of this project is to create an app using Python and Kivy to show tidal information.

## Installation
Setup terminal and pip
```
python3 -m pip install --upgrade pip setuptools virtualenv
```
Create the python virtual environment
```
python3 -m virtualenv kivy_venv
```
Activate the virtual environment
```
source kivy_venv/bin/activate
```
Install Kivy
```
python3 -m pip install kivy[base] kivy_garden.graph
```
Copy the kivy application files into the virtual environment folder
```
cp main.py kivy_venv/
```
Run the application
```
python3 kivy_venv/main.py
```
You should get a happy Kivy window with some graphics. Otherwise, Kivy will show you a log in the terminal with your build errors.

## Troubleshooting
I have been developing this application on Ubuntu 20.04 by way of WSL2, which has been *challenging*. The main headache is running an X11 server on the Windows host, and getting direct rendering of OpenGL to pass to the host machine. If you are on macOS or Ubuntu, your mileage may vary.

### WSL2 Issues
**WSL2**
To start, make sure you are using WSL2 and not WSL1. Depending on when you installed Ubuntu from the Microsoft App Store, you may or may not be on 1. For more information, refer to Microsoft's installation documentation: https://docs.microsoft.com/en-us/windows/wsl/install-win10


**Ubuntu Version**
You must use a minimum of Ubuntu 20.04. Kivy requires at least OpenGL v2 to render graphics. Out of the box, you will see Kivy build errors complaining about being limited to OpenGL v1.4 and being forced to use indirect rendering. Refer to this Github Issue: https://github.com/microsoft/WSL/discussions/6154. Specifically, add the mesa drivers referenced by Trass3r.


**X11 Server**
You must use an X11 Server on the Windows side to use Kivy. I had installed it before developing in order to build xTide on WSL2. I found a helpful blog post on how to do this with Windows. Headaches include updating your Windows Firewall to allow traffic from WSL2, which does not use a static IP.


**Testing OpenGL settings**
Once you have the correct version of Ubuntu, a functioning X11 server, and the mesa drivers needed to run OpenGL > v2, you can easily test it by running the following command.
```
glxinfo -B
``` 
The resulting information should tell you if direct rendering is in use, what driver is facilitating direct rendering, and what version of OpenGL is detected. If direct rendering is not in use, try the following command, and run glxinfo again.
```
export LIBGL_ALWAYS_INDIRECT=0
```
Supposedly, WSL2 has a config file set to force this value to be '1'. Other posts I read claimed one could set this in .bashrc. I found that setting the above command in .bashrc does not work as intended, but sourcing .bashrc then does work. Strange WSL2 ghosts, and I have not solved that issue as I want to move on to actually developing this application.

One last word about OpenGL version. The version supported by Windows is determined by the graphics drivers. If you use an integrated graphics chip, then you need to update the drivers for your CPU. If you have a graphics card, you need to make sure those graphics drivers are up-to-date AND that Windows is defaulting to those drivers when using OpenGL. I had to download the Nvidia Control Panel to force my Windows to use those drivers.

## Resources
### Kivy Application Framework
-Kivy Documentation: https://kivy.org/doc/stable/
-Kivy Docs - Installing Kivy: https://kivy.org/doc/stable/gettingstarted/installation.html
-Kivy Docs - API Reference: https://kivy.org/doc/stable/api-kivy.html
-Kivy Garden: https://github.com/kivy-garden
-Kivy Garden - Graphs: https://github.com/kivy-garden/graph

### xTide
-xTide Source Code: https://flaterco.com/xtide/xtide.html
-tidepredict: https://github.com/windcrusader/tidepredict

### WSL2 
-Installation and Upgrade docs: https://docs.microsoft.com/en-us/windows/wsl/install-win10
-Install X11 Server: https://thomasward.com/wsl2-x11/
-Fixing OpenGL Direct Rendering version: https://github.com/microsoft/WSL/discussions/6154
-Mesa Drivers: https://launchpad.net/~oibaf/+archive/ubuntu/graphics-drivers/ 
