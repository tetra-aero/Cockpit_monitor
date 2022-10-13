#!/usr/bin/env python3
"""can_recv_draw.py
- Usage
$ python3 can_recv_draw.py
"""
#__all__ = ['sys']
__author__ = "Yoshio Akimoto <yoshio.akimoto@tetra-aviation.com>, Yoshihiro Nakagawa <yoshihiro.nakagawa@tetra-aviation.com>"
__date__ = "14 October 2022"

__version__ = "1.0.0"
__credits__ = "teTra Aviation Corp."

import sys
import os.path
import string
import re

import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import can


esc_data_v = np.zeros(32)
esc_throttle = np.zeros(32)


class PlotGraph:
    def __init__(self):
          
        # UIを設定
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('ESC Voltage')
        self.win.resize(800,600)
        self.plt = self.win.addPlot()
        self.plt.setXRange(0, 32)
        #self.plt.setYRange(0, 50)
        self.plt.setYRange(30, 56)
        self.curve = self.plt.plot(pen=(0, 0, 255))


        # データを更新する関数を呼び出す時間を設定
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        #self.data = np.zeros(32)
        esc_data_v = np.zeros(32)

    #graphic data update
    def update(self):

        #Making 32 sample datas (Random)
        #for i in range(0, 32):
        #    self.data[i] = self.voltage_list[i] + np.random.rand() * 5
        x = np.arange(32)
        #y1 = np.linspace(0, 20, num=64)

        #棒グラフ描画
        # <!> 重要 : プロットを描画する前に、古い描画を消しておく（重ね描きになってしまう） 
        self.plt.clear()
        # data配列をデータとした、緑の棒グラフを作成
        bg1 = pg.BarGraphItem(x=x, height=esc_data_v, width=0.6, brush='g')
        self.plt.addItem(bg1)

class PlotGraph2:
    def __init__(self):
        
        # UIを設定 2
        self.win2 = pg.GraphicsWindow()
        self.win2.setWindowTitle('ESC throttle')
        self.plt2 = self.win2.addPlot()
        self.plt2.setXRange(0, 32)
        self.plt2.setYRange(0, 1000)
        self.curve2 = self.plt2.plot(pen=(0, 0, 255))

        # データを更新する関数を呼び出す時間を設定
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        #self.data = np.zeros(32)
        esc_throttle = np.zeros(32)


    #graphic data update
    def update(self):

        #Making 32 sample datas (Random)
        #for i in range(0, 32):
        #    self.data[i] = self.voltage_list[i] + np.random.rand() * 5
        x = np.arange(32)
        #y1 = np.linspace(0, 20, num=64)

        #棒グラフ描画
        # <!> 重要 : プロットを描画する前に、古い描画を消しておく（重ね描きになってしまう） 
        self.plt2.clear()
        # data配列をデータとした、赤の棒グラフを作成
        bg2 = pg.BarGraphItem(x=x, height=esc_throttle, width=0.6, brush='r')
        self.plt2.addItem(bg2)



# CANバスの初期化 (#6,#7は未実装。予備)
bus1 = can.interface.Bus(channel = 'can_spi0.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus2 = can.interface.Bus(channel = 'can_spi0.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus3 = can.interface.Bus(channel = 'can_spi1.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus4 = can.interface.Bus(channel = 'can_spi1.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus5 = can.interface.Bus(channel = 'can_spi1.2', bustype='socketcan', bitrate=125000, canfilters=None)
#bus6 = can.interface.Bus(channel = 'can_spi2.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus7 = can.interface.Bus(channel = 'can_spi2.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus1 = can.interface.Bus(channel = 'vcan0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus1 = can.interface.Bus(channel = 'vcan_spi0.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus2 = can.interface.Bus(channel = 'vcan_spi0.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus3 = can.interface.Bus(channel = 'vcan_spi1.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus4 = can.interface.Bus(channel = 'vcan_spi1.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus5 = can.interface.Bus(channel = 'vcan_spi1.2', bustype='socketcan', bitrate=125000, canfilters=None)
#bus6 = can.interface.Bus(channel = 'vcan_spi2.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus7 = can.interface.Bus(channel = 'vcan_spi2.1', bustype='socketcan', bitrate=125000, canfilters=None)

# すでに用意されているコールバック関数(can.Listenerクラスのon_message_received関数)をオーバーライド
class CallBackFunction(can.Listener):
  def on_message_received(self, msg):
#    print("hoge")
#    print(hex(msg.arbitration_id))
#    print(msg)
#    print(msg.data)
#    print(msg.data.hex())

    #Making 32 sample datas (Random)
    #for i in range(0, 32):
    #    esc_data_v[i] = 40 + np.random.rand() * 5

    #ESC Volt (ID=0x13) Pickup
    if re.search("0x13", hex(msg.arbitration_id)) != None:
        #print(msg)
        #ESC ID
        #print(hex(msg.arbitration_id)[-2:])
        #ESC Volt data
        #print((msg.data.hex())[1:])

        #Making 32 sample datas (Random)
        #for i in range(0, 32):
        #    esc_data_v[i] = 40 + np.random.rand() * 5

        esc_data_v[int(hex(msg.arbitration_id)[-2:],16)] = int((msg.data.hex())[1:],16)/10


    #ESC Volt (ID=0x13) Pickup
    if re.search("0x20", hex(msg.arbitration_id)) != None:
        print(msg)
        #ESC ID
        #print(hex(msg.arbitration_id)[-2:])
        #ESC Volt data
        #print((msg.data.hex())[1:])

        esc_throttle[int(hex(msg.arbitration_id)[-2:],16)] = int((msg.data.hex())[1:],16)

# コールバック関数のインスタンス生成
call_back_function = CallBackFunction()

# コールバック関数登録
can.Notifier(bus1, [call_back_function, ])
#can.Notifier(bus2, [call_back_function, ])
#can.Notifier(bus3, [call_back_function, ])
#can.Notifier(bus4, [call_back_function, ])
#can.Notifier(bus5, [call_back_function, ])
#can.Notifier(bus6, [call_back_function, ])
#can.Notifier(bus7, [call_back_function, ])


# 何もしない処理（受信のコールバックのみ）
if __name__ == "__main__":
    graphWin = PlotGraph()
    graphWin2 = PlotGraph2()
    #graphWin3 = PlotGraph2()
    #graphWin4 = PlotGraph2()
    #graphWin5 = PlotGraph2()
    #graphWin6 = PlotGraph2()
    #graphWin = main()   
    
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

#except KeyboardInterrupt:
        print('exit')
        bus1.shutdown()
#        bus2.shutdown()
#        bus3.shutdown()
#        bus4.shutdown()
#        bus5.shutdown()
##  bus6.shutdown()
##  bus7.shutdown()
  
  
