#!/bin/sh
sudo ip link set dev can_spi0.0 down
sudo ip link set dev can_spi0.1 down
sudo ip link set dev can_spi1.0 down
sudo ip link set dev can_spi1.1 down
sudo ip link set dev can_spi1.2 down

#sudo modprobe -r mcp251xfd
#sudo modprobe mcp251xfd

sudo ip link set dev can_spi0.0 type can bitrate 125000
sudo ip link set dev can_spi0.1 type can bitrate 125000
sudo ip link set dev can_spi1.0 type can bitrate 125000
sudo ip link set dev can_spi1.1 type can bitrate 125000
sudo ip link set dev can_spi1.2 type can bitrate 125000

sudo ifconfig can_spi0.0 txqueuelen 1000
sudo ifconfig can_spi0.1 txqueuelen 1000
sudo ifconfig can_spi1.0 txqueuelen 1000
sudo ifconfig can_spi1.1 txqueuelen 1000
sudo ifconfig can_spi1.2 txqueuelen 1000

#cangw -A -s can_spi1.2 -d can_spi0.0 -e
#cangw -A -s can_spi1.2 -d can_spi0.1 -e
#cangw -A -s can_spi1.2 -d can_spi1.0 -e
#cangw -A -s can_spi1.2 -d can_spi1.1 -e

#cangw -A -s can_spi0.0 -d can_spi1.2 -e
#cangw -A -s can_spi0.1 -d can_spi1.2 -e
#cangw -A -s can_spi1.0 -d can_spi1.2 -e
#cangw -A -s can_spi1.1 -d can_spi1.2 -e

sudo ip link set dev can_spi0.0 up
sudo ip link set dev can_spi0.1 up
sudo ip link set dev can_spi1.0 up
sudo ip link set dev can_spi1.1 up
sudo ip link set dev can_spi1.2 up
