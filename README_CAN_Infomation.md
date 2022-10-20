# Draft of Gachacon CAN Bus Protocol

# teTra Mk-5 SN4
TBD......

# teTra Mk-5 SN3

## 2. ESC-UART, information Voltage (Battery Voltage, Throttle, Act throttle, Bus current, Phase current)
- CAN ID, 0x1300 - 0x131F
  - 0x1300: Serial number of GachaconECU No.0
  - 0x1301: Serial number of GachaconECU No.1
  - ......
  - 0x131F: Serial number of GachaconECU No.31
- Data, Ranage: 0x0000 - 0x01770 (0 - 0600)
  - Battery Voltage, 00.0 - 60.0 [V]

### 2.1 ESC-UART, Throttle
- CAN ID, 0x2000 - 0x201F
  - 0x2000: Serial number of GachaconECU No.0
  - 0x2001: Serial number of GachaconECU No.1
  - ......
  - 0x201F: Serial number of GachaconECU No.31
- Data, Ranage:
  - Throttle

### 2.2 ESC-UART, Act throttle
- CAN ID, 0x2100 - 0x211F
  - 0x2100: Serial number of GachaconECU No.0
  - 0x2101: Serial number of GachaconECU No.1
  - ......
  - 0x211F: Serial number of GachaconECU No.31
- Data, Ranage:
  - Act throttle

### 2.3 ESC-UART, Bus current
- CAN ID, 0x2200 - 0x221F
  - 0x2200: Serial number of GachaconECU No.0
  - 0x2201: Serial number of GachaconECU No.1
  - ......
  - 0x221F: Serial number of GachaconECU No.31
- Data, Ranage:
  - Bus current

### 2.4 ESC-UART, Phase current
- CAN ID, 0x2300 - 0x231F
  - 0x2300: Serial number of GachaconECU No.0
  - 0x2301: Serial number of GachaconECU No.1
  - ......
  - 0x231F: Serial number of GachaconECU No.31
- Data, Ranage:
  - Phase current

## 4. Information, Warnning and Error code

### 4-1, 0x8000, information of ECU Boot
- CAN ID, 0x8000 - 0x801F
  - 0x8000: Serial number of GachaconECU No.0
  - 0x8001: Serial number of GachaconECU No.1
  - ......
  - 0x801F: Serial number of GachaconECU No.31
- Data: A5
- Response: No

### 4-2, 0x8100/0x8200 information of CAN BUS Health check
- CAN ID, 0x8100 - 0x811F
  - 0x8000: Serial number of GachaconECU No.0
  - 0x8001: Serial number of GachaconECU No.1
  - ......
  - 0x801F: Serial number of GachaconECU No.31
- Data: A5
- Response: Yes
- CAN ID, 0x8200 - 0x821F
  - 0x8200: Serial number of GachaconECU No.0
  - 0x8201: Serial number of GachaconECU No.1
  - ......
  - 0x821F: Serial number of GachaconECU No.31
- Data: 
  - Health Success: 5A
  - Health Fail: FF
