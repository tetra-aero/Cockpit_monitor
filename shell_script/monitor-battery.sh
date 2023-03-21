#!/bin/sh
#candump can_spi0.0 can_spi0.1 can_spi1.0 can_spi1.1 can_spi1.2 |tee can_`date +%F_%T`.log | python3 $HOME/.local/share/candump-display-escdata.py
candump can_spi0.0 can_spi0.1 can_spi1.0 can_spi1.1 can_spi1.2 | python3 ./candump-display-escdata.py
