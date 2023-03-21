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
    ## 読み込んだバイナリファイルを表示し終わるまでループします
    #for byte in read_bytes(file_path):
    for line in fileinput.input():
        #print("debug: " + line)
        #000013: CANID_ESC_voltage
        #000020: CANID_ESC_throttle
        #000021: CANID_ESC_act_throttle
        #000022: CANID_ESC_bus_current
        #000023: CANID_ESC_phase_current
		#000080: CANID_CANBUS_boot ECU
        #000081: CANID_CANBUS_Health_ask
        #000082: CANID_CANBUS_Health_res
        if re.search("000080", line) != None:
            num_command = re.search("000080", line)
            print("debug: " + line)
            #pos_com13 = num_command.span()
            #num_gachacon = int(line[pos_com13[1]], base = 16) * 16  + int(line[pos_com13[1]+1], base = 16)
            #num_length = int(pos_com13[1]+6)
        else:
            None
        # end if
    # end for
# end def

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit(0)

