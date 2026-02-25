import pyshark
import string

# https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4
def map_keystrokes(keystroke_data):
    newmap = {
     1: "ErrorRollOver",
     2: "PostFail",
     4: "a",
     5: "b",
     6: "c",
     7: "d",
     8: "e",
     9: "f",
     10: "g",
     11: "h",
     12: "i",
     13: "j",
     14: "k",
     15: "l",
     16: "m",
     17: "n",
     18: "o",
     19: "p",
     20: "q",
     21: "r",
     22: "s",
     23: "t",
     24: "u",
     25: "v",
     26: "w",
     27: "x",
     28: "y",
     29: "z",
     30: "!", 
     31: "2",
     32: "3",
     33: "4",
     34: "5",
     35: "6",
     36: "7",
     37: "8",
     38: "9",
     39: "0",
     40: "Enter",
     41: "esc",
     42: "del",
     43: "tab",
     44: "space",
     45: "_",
     47: "{",
     48: "}",
     50: "#",
     51: "esc",
     52: 'Shift',
     54: ",",
     55: '.',
     56: "/",
     57: "CapsLock",
     79: "RightArrow",
     80: "LetfArrow"
     }

    key_presses = []

    prev_keys = set()

    for line in keystroke_data:
        bytesArray = bytearray.fromhex(line.strip())
        check_for_upper = set(bytesArray[0:2])
        current_keys = set(bytesArray[2:8])
        current_keys.discard(0)

        new_keys = current_keys - prev_keys

        for keyVal in new_keys:
            if keyVal in newmap:
                key_presses.append(newmap[keyVal])
            else:
                print("No map found for this value: " + str(keyVal))

        prev_keys = current_keys

    mstr = []
    active_caps = False

    for _keypress in key_presses:

        if _keypress == 'CapsLock':
            active_caps = not active_caps

        if _keypress in string.printable:
                if active_caps:
                    mstr.append(_keypress.upper())
                else:
                    mstr.append(_keypress)

        elif _keypress == 'space':
            mstr.append(' ')

        elif _keypress == 'del':
            if mstr:
                mstr.pop()

        elif _keypress == 'Enter':
            mstr.append('\n')

        elif _keypress == 'esc':
            mstr.append(' ESC ')


    print(''.join(mstr))


cap = pyshark.FileCapture(
    r"C:\Users\Samuele\Documents\FIles Olicyber\USB Password\keylogger.pcap",
    display_filter="usb.transfer_type == 0x01"
)

key_data = []
for pkt in cap:
    cap_data = pkt.data.usb_capdata.replace(":", "")
    key_data.append(cap_data)

map_keystrokes(key_data)

#flag{USB_k3yl0gger!}