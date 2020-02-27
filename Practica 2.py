import os
'''
hostname="www.itmorelia.edu.mx"
respuesta=os.system("ping -c 1" + hostname)
if respuesta==0:
    print(hostname + ": está en funcionamiento!")
else:
    print (hostname + ": No funciona!")
'''
red="200.33.171.0/24"
os.system("nmap -sP " + red)
'''
[fernando@pc ~]$ /usr/bin/python "/home/fernando/python/Practica 2.py"
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:52 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.0065s latency).
Nmap scan report for 200.33.171.13
Host is up (0.010s latency).
Nmap scan report for sagitario.itmorelia.edu.mx (200.33.171.65)
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.66
Host is up (0.014s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.024s latency).
Nmap scan report for 200.33.171.85
Host is up (0.019s latency).
Nmap scan report for 200.33.171.120
Host is up (0.0046s latency).
Nmap scan report for 200.33.171.125
Host is up (0.011s latency).
Nmap done: 256 IP addresses (8 hosts up) scanned in 4.46 seconds
'''
