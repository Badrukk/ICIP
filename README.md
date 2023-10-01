# ICIP
*I see IP...*

A very simple script that uses the strings command in Linux to extract strings from binaries. It uses regular expressions to filter the output so that the console prints out:
- IPv4 addresses
- Website addresses
- MAC addresses
- Email addresses

Usage is the following:
> sudo python ICIP.py /path/binary

> sudo python ICIP.py /dev/mem

> sudo python ICIP.py /path/*
