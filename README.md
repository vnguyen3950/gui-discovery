# gui-discovery
## Installation
### Requirements
- [Docker](https://www.docker.com/products/docker-desktop)
- [XCVSrv for Windows machines](https://sourceforge.net/projects/vcxsrv/)
- [VSCode](https://code.visualstudio.com/) with Docker/Remote Development extension
### Steps
  - Open XCVSrv (XLaunch)
    - Set the following and keep everything else the same
    - Multiple Display option
    - Start No Client option
    - Check Disable Access Control
  - Open the folder in a container in VSCode using the green button on the bottom left
  - Set DISPLAY environment variable in container terminal ``` DISPLAY=[your machine's local ip]:0 ```
    - Example: ``` DISPLAY=192.168.1.1:0 ```
  - Run the Drag n Drop program with ``` python3 dragndropv2.py ```