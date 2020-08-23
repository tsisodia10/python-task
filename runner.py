#!/usr/bin/env python3

#
#          FILE:  runner.py
#
#
#   DESCRIPTION:  Manage rules
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#        AUTHOR:  Twinkll Sisodia
#       COMPANY:  Red Hat
#       VERSION:  1.0
#       CREATED:  08/21/2020
# ===============================================================================

import argparse
import os
import subprocess
import sys


parser = argparse.ArgumentParser(description='Manage rules')

parser.add_argument('-c', '--count', 
                     metavar='count', action='count', 
                     required=True, add_help=True)

parser.add_argument('-fc', '--failed-count', 
                     action='store', 
                     required=True) 

args = parser.parse_args()

#add rules
if (args.count>1):
      print("Count -",sys.argv)
      exitCode = os.system(f'ping -c {args.count} google.com')
      if exitCode == 0:
          print("Success")
          print("Tracing Successful execution --------------------------------------------------------\n")
          pingParsing = os.system(f'pingparsing google.com -c {args.count}')
          print(pingParsing)
      else: 
          while args.failed >= 2:
            exitCode = os.system(f'ping -c {args.count} google.com')
          print("ExitCode ----- \n",exitCode)
          
          print("Tracing memory usage of failed execution -----------------------------------------------------------\n")
          sysTrace = os.system(f'strace ping -c {args.count} google.com')
          print("/n/n/n")
          print("Tracing Failed execution -----------------------------------------------------------\n")
          pingParsing = os.system(f'pingparsing google.com -c {args.count}')
          print(sysTrace)
          print(pingParsing)