# Cockpit_monitor
Cockpit panel GUI teTra Mk-5

## Example
- v1.0
![V1.0 volatage and throttle](/document/221014_v1p0_vcan_votage_throttle.png)

## Requirement
```
sudo apt install can-utils
sudo apt install net-tools
pip3 install python-can
```

## Debug
### case of vertual can port
- terminal 1
```
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 type can bitrate 125000
sudo ip link set up vcan0
cd log_candata/
canplayer vcan0=can_spi0.0 vcan0=can_spi0.1 vcan0=can_spi1.0 vcan0=can_spi1.1 vcan0=can_spi1.2 -I ./candump-2022-02-22_161128_test03-04.log
```

- terminal 2
```
python3 v1p0_virtual_can/python3 can_recv_draw.py 
```

### case of physical can port
- terminal 1
```
sudo ifconfig can0 txqueuelen 1000
sudo ip link set can0 type can bitrate 125000
sudo ip link set up can0
cd log_candata/
canplayer can0=can_spi0.0 can0=can_spi0.1 can0=can_spi1.0 can0=can_spi1.1 can0=can_spi1.2 -I ./candump-2022-02-22_161128_test03-04.log
```

- terminal 2
```
python3 can_recv_draw.py 
```

### Reference
- https://gist.github.com/takurx/e19c1dbeba413e5a24337b98defc60a7
- https://gist.github.com/takurx/9b324a2d47442c78b3474c87b34bae59
