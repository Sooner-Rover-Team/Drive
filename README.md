# manual_operate

This code can drive the rover, move the arm, and operate the science package. It requires an XBOX or PS4/PS5 controller to operate.

## Dependencies
At the moment, python 3.10 or higher, pygame and zmq are required to run manual_operate.py.

Python can be downloaded [here](https://www.python.org/downloads/)

Download the libraries using 
```
pip install pygame 
pip install zmq
```

## Usage

The config.ini file must have the correct ip addresses of the EBOX microcontroller, as it controls the wheels and distributes data to arm/science via CAN-Bus.

Ebox Teensy 4.1 IP: 192.168.1.101
Ebox Teensy 4.1 Port: 1001

The controller configuration can also be adjusted according to the physical controller being used. In config.ini, change `[Controller] CONFIG = ` to `ps` or `xbox`

## Controls

There are two distinct modes in the program: drive and operate. Drive obviously just drives the wheels and changes LEDs. Operate can be used to control either the science package or the arm, depending on which is installed (can be toggled by pressing **Select**). **B** switches between drive and operate.

### Drive

The rover drives with tank controls (**Left Stick** moves left wheels, **Right Stick** moves right wheels). The **Left Bumper** will only move the front wheels while the **Right Bumper** will only move the back wheels. This could be useful for getting the rover unstuck. **A** will just make the lights flash. 

### Arm

The arm is controlled with the help of the GUI. The **Left Stick** controls the point of the wrist in space and the actuators will automatically adjust their length to keep the wrist on that point. The **Right Stick** controls the tilt and rotation of the wrist. The operator must be careful not to overtwist the wrist as the cords can get tangled and disconnected if the wrist is rotated too far. **A** opens and closes the claw. **Left Trigger** rotates the base to the left while **Right Trigger** rotates the base to the right.

### Science Package

The Science package has 4 distinct controllable elements. The **Left Stick** moves the drill up and down in space. The **Right Stick** controls the speed of the drill. **Right Trigger** increases the speed of the vacuum while **Left Trigger** decreases it. **Left Bumper** rotates the carousel clockwise while **Right Bumper** rotates the carousel counterclockwise. **A** attempts to move the carousel one seventh of a rotation, but it is based on time elapsed and may not move the same amout each time.
