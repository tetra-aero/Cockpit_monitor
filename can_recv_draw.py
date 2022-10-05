# example: $ candump can1 | python3 candump-display-escdata.py
#
# chiya@ujimatsu:~/JetsonWorks/file-pyserial-uart-simulator/binary_data$ candump can1 | python3 candump-display-escdata.py
# 
# #### BINARY TO HEX DUMP - USING PYTHON3.6 ####
# 
# Offset 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F Encode to ASCII
# 
# debug:   can1  0000160F   [2]  17 70
# 
# Gachacon Num.: 15, Battery: 119.04761904761904 %, 60.0 V
# 

import sys
import os.path
import string
import re

import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import can


esc_data_v = np.zeros(32)


class PlotGraph:
    def __init__(self):
	# Initialize other
        self.voltage_list = np.zeros(32)
        throttle = act_throttle = voltage = bus_current = phase_current = 0
        num_gachacon = 0
        num_voltage = 0
        num_bat_persentage = 0.0

        for i in range(0, 32):
            self.voltage_list[i] = 40
            
        # UIを設定
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle('ESC Voltage plot')
        self.plt = self.win.addPlot()
        #self.plt.setYRange(0, 1)
        self.plt.setYRange(0, 50)
        self.curve = self.plt.plot(pen=(0, 0, 255))

        # データを更新する関数を呼び出す時間を設定
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        #self.data = np.zeros(32)
        esc_data_v = np.zeros(32)

    #graphic data update
    def update(self):
        #棒グラフ描画
        # <!> 重要 : プロットを描画する前に、古い描画を消しておく（重ね描きになってしまう） 
        self.plt.clear()

        #Making 32 sample datas (Random)
        #for i in range(0, 32):
        #    self.data[i] = self.voltage_list[i] + np.random.rand() * 5
        x = np.arange(32)
        #y1 = np.linspace(0, 20, num=64)

        # data配列をデータとした、緑の棒グラフを作成
        bg1 = pg.BarGraphItem(x=x, height=esc_data_v, width=0.6, brush='g')
        self.plt.addItem(bg1)



# CANバスの初期化 (#6,#7は未実装。予備)
bus1 = can.interface.Bus(channel = 'can_spi0.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus2 = can.interface.Bus(channel = 'can_spi0.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus3 = can.interface.Bus(channel = 'can_spi1.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus4 = can.interface.Bus(channel = 'can_spi1.1', bustype='socketcan', bitrate=125000, canfilters=None)
#bus5 = can.interface.Bus(channel = 'can_spi1.2', bustype='socketcan', bitrate=125000, canfilters=None)
#bus6 = can.interface.Bus(channel = 'can_spi2.0', bustype='socketcan', bitrate=125000, canfilters=None)
#bus7 = can.interface.Bus(channel = 'can_spi2.1', bustype='socketcan', bitrate=125000, canfilters=None)

# すでに用意されているコールバック関数(can.Listenerクラスのon_message_received関数)をオーバーライド
class CallBackFunction(can.Listener):
  def on_message_received(self, msg):
#    print("hoge")
#    print(hex(msg.arbitration_id))
#    print(msg)
#    print(msg.data)
#    print(msg.data.hex())


    #ESC Volt (ID=0x13) Pickup
    if re.search("0x13", hex(msg.arbitration_id)) != None:
        print(msg)
        #ESC ID
        #print(hex(msg.arbitration_id)[-2:])
        #ESC Volt data
        #print((msg.data.hex())[1:])

        #Making 32 sample datas (Random)
        #for i in range(0, 32):
        #    esc_data_v[i] = 40 + np.random.rand() * 5


        esc_data_v[int(hex(msg.arbitration_id)[-2:],16)] = int((msg.data.hex())[1:],16)/10


    #Making 32 sample datas (Random)
    #for i in range(0, 32):
    #    esc_data_v[i] = 40 + np.random.rand() * 5



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
  
  
