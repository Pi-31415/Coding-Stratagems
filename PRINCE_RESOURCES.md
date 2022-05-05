## Resources from Prince

### Interview Questions (Struct vs Class) 
- https://www.geeksforgeeks.org/structures-in-cpp/
- In class, it's private or public.
- In struct, everything is public.

## How to see who call the function
- In ROS call log in debug mode, provide their name

## Mutex vs Semaphore
- Locking access abstraction
- https://www.geeksforgeeks.org/mutex-vs-semaphore/
- Issues : https://docs.oracle.com/cd/E19120-01/open.solaris/816-5137/6mba5vq11/index.html#:~:text=A%20problem%20exists%20if%20two,to%20lock%20the%20other%20mutex.

VirtualBox fakes the hardware, the containers fake the Operating System

- bare metal hypervisor
- kubernetes for container
- neofetch for system information

### How to see pre compiled C++ file
```
g++ -E first.cpp>pre   
```

```
Compile the code into assembly
g++ -S first.cpp
```

```
Compile the code into assembly
g++ -c first.cpp
```

Unnamed scope exists in C++

CMakeLists.txt

-std tag = choose c++ version

Makefile
Full Tutorial : https://makefiletutorial.com/
https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html

## Monitoring Processes on Computers 
- brew install bpytop

### Theory

Instruction Set Architecture

### IP Address
On Windows
```
ipconfig
```
On Linux
```
ifconfig
```
To send fake packet to system
```
ping
```

## File Sharing Protocols

-Use Samba Linux (https://www.samba.org/)
-Apple Filing Protocol (AFP) on MacOS
-FTP


### Daemon in Linux to inspect samba file sharing protocol

```
sudo systemctl samba
```

On Windows, using Samba is to run and 
```
\\10.224.10.24
```

On Mac, using Samba is to go to Finder -> Go -> Connect to server

On Android, cx file explorer.


To share files within macos

## FTP Open Source
Clonezilla

# Get Bash History
On Mac, control+R and find the research search

# How to access quick sudo
Add
```
sudo !!
```
And append sudo to previous command.

## Public vs Protected
https://www.geeksforgeeks.org/difference-between-private-and-protected-in-c-with-example/

## C++ Custom keywords
- Wow, you can create your own keywords.

## Lubuntu - lightweight OS

Most of the times, you don't want to use dynamic memory allocation
