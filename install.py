# This program is a part of EASIFEM library.
# See. www.easifem.com
# Copyright (c) 2020-2021, All right reserved, Vikas Sharma, Ph.D.
#

import os
import sys
import platform

def installRequest(LIB):
    while True:
        choice = input(f"Do you want to Install {LIB} 'yes' or 'no' [Y/n]: ")
        if( choice == " "):
          choice="no"
        else:
          choice=choice.lower()
        if choice in ['Y', 'y', 'ye', 'yes']:
          return True
        else:
          return False

def getOption(key, opt):
  while True:
    separator = ', '
    return input( f"select option for {key}, possible options are : {separator.join(opt)} : ") + " "

print("Detecting OS type...")
_os = platform.system()
if _os == 'Windows':
    print("ERROR: INSTALLATION on windows is work in progress")
    exit
    #print("Please use Windows Subsystem Linux(WSL) ")
    #print("Installation DONE!!")
else:
    cmake_def = " -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=${EASIFEM_EXTPKGS}"
    print( "CMAKE DEF : ", cmake_def )
    os.system( f"cmake -S ./ -B ./build {cmake_def}")
    os.system(f"cmake --build ./build --target install" )
    print("Installation DONE!!")
