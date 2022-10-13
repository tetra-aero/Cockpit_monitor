# Cockpit_monitor
Cockpit panel GUI

## Debug
```
sudo ifconfig can0 txqueuelen 1000
sudo ip link set can0 type can bitrate 125000
sudo ip link set up can0
cd log_candata/
canplayer can0=can_spi0.0 can0=can_spi0.1 can0=can_spi1.0 can0=can_spi1.1 can0=can_spi1.2 -I ./candump-2022-02-22_161128_test03-04.log
```
