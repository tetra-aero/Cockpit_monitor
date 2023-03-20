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
import fileinput
import re

def check_file_provided():
    # 指定した先にファイルが存在するかをチェック
    default_path = "./test.exe"

    if (len(sys.argv) < 2):
        print("")
        print("Warning")
        print("Correct Usage : python read_bin.py <file_name>")
        print("")
        print("call {0}".format(default_path))
        if not os.path.isfile(default_path):
            print("")
            print("Error - The file provided does not exist")
            print("")
            sys.exit(0)
        else:
            print("{} is exist".format(default_path))
            print("")

            return default_path
    else:
        print("")
        print("{} is exist".format(sys.argv))
        print("")

        return sys.argv[1]

def print_headers():
    ## とりあえずフォーマット的なものを表示する
    print("")
    print("#### BINARY TO HEX DUMP - USING PYTHON3.6 ####")
    print("")
    print("Offset 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F Encode to ASCII")
    print("")

def main():
    #print_headers()
    throttle = act_throttle = voltage = bus_current = phase_current = 0
    num_gachacon = 0
    num_voltage = 0
    num_bat_persentage = 0.0

    for i in range(0, 32):
        #print("Gachacon Num.: " + str(i) + ", 00.0 V, Battery: 000.00 %")
        #print("Gachacon Num.: %2d, %2.1f V, Battery: %2.2f %", num_gachacon, num_voltage, num_bat_persentage)
        print('Gachacon Num.: {0:2}, {1:4.1f} V, Battery: {2:5.2f} %'.format(i, num_voltage, num_bat_persentage))
        #print('Gachacon Num.: {0:2}, {1:2.1f} V, Battery: {2:2.2f} %\033[1A'.format(i, num_voltage, num_bat_persentage))
        #print("\033[2A")
    #print("\033[33A")
    #i = 10
    #print("\033[{}B".format(i-1))
    #print("\033[{}B".format(31-i))
    
    ## 読み込んだバイナリファイルを表示し終わるまでループします
    #for byte in read_bytes(file_path):
    for line in fileinput.input():
        #print("debug: " + line)
        #000013: CANID_ESC_voltage
        #000020: CANID_ESC_throttle
        #000021: CANID_ESC_act_throttle
        #000022: CANID_ESC_bus_current
        #000023: CANID_ESC_phase_current
        #000081: CANID_CANBUS_Health_ask
        #000082: CANID_CANBUS_Health_res
        if re.search("000013", line) != None:
            num_command = re.search("000013", line)
            #print("debug: " + str(num_command))
            pos_com13 = num_command.span()
            #print("debug: start, " + str(pos_com13[0]))
            #print("debug: end, " + str(pos_com13[1]))
            #  vcan_spi0.0  00001300   [2]  01 CE
            #-> '000013' -> 15,21
            #  can0  00001300   [2]  01 CE
            #-> '000013' -> 8,14 -> 24
            #print("debug: " + line[14])
            #print("debug: " + line[15])
            num_gachacon = int(line[pos_com13[1]], base = 16) * 16  + int(line[pos_com13[1]+1], base = 16)
            #print("debug: " + "Gachacon Number: " + str(num_gachacon))
            
            #print("debug: " + line[20])
            num_length = int(pos_com13[1]+6)
            #print("debug: " + "Length: " + str(num_length))

            #print("debug: " + line[24])
            #print("debug: " + line[25])
            #print("debug: " + line[27])
            #print("debug: " + line[28])
            num_voltage =  (int(line[pos_com13[1]+10], base = 16) * 16  * 16  * 16 + \
                            int(line[pos_com13[1]+11], base = 16) * 16  * 16 + \
                            int(line[pos_com13[1]+13], base = 16) * 16  + \
                            int(line[pos_com13[1]+14], base = 16)) / 10.0
            #print("debug: " + "Voltage: " + str(num_voltage))

            # Li-Po battery range: 4.2-3.2, 12 cells
            # 4.2 * 12 = 50.4, 4.25 * 12 = 51.0, ,3.2 * 12 = 38.4, 50.4 - 38.4 = 12.0
            #num_bat_persentage = (num_voltage - (3.2 * 12)) / ((4.25 * 12) - (3.2 * 12)) * 100
            num_bat_persentage = (num_voltage - 38.4) / 12.0 * 100
            if num_bat_persentage > 100.0:
                num_bat_persentage = 100.0
            #print("debug: " + "Battery: " + str(num_bat_persentage) + " %")
            #print("Gachacon Num.: " + str(num_gachacon) + ", " + str(num_voltage) + " V, Battery: " + str(num_bat_persentage) + " %")
            print("\033[33A")
            if num_gachacon > 0:
                print("\033[{}B".format(num_gachacon))
                print("\033[2A")
            #print("Gachacon Num.: %2d, %2.1f V, Battery: %2.2f %", num_gachacon, num_voltage, num_bat_persentage)
            print('Gachacon Num.: {0:2}, {1:2.1f} V, Battery: {2:2.2f} %'.format(num_gachacon, num_voltage, num_bat_persentage), end="")
            if num_gachacon < 32:
                print("\033[{}B".format(32-num_gachacon))
                print("\033[2A")
                #if num_gachacon >= 30:
                #print("\033[1A")
                #pass
            #pass
        else:
            None
            #print("debug: " + line)
        # end if
    # end for
# end def

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit(0)

