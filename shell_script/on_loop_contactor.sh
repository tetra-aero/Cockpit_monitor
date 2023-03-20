#!/bin/sh

while true
do
	sleep 1
	cansend can_spi0.1 000012FF#C0
	cansend can_spi0.0 000012FF#C0
	cansend can_spi1.1 000012FF#C0
	cansend can_spi1.0 000012FF#C0
done

