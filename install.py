# This program is a part of EASIFEM library.
# See. www.easifem.com
# Copyright (c) 2020-2021, All right reserved, Vikas Sharma, Ph.D.
#

import os

# import sys
import platform


def installRequest(LIB):
    while True:
        choice = input(f"Do you want to Install {LIB} 'yes' or 'no' [Y/n]: ")
        if choice == " ":
            choice = "no"
        else:
            choice = choice.lower()
        if choice in ["Y", "y", "ye", "yes"]:
            return True
        else:
            return False


def getOption(key, opt):
    while True:
        separator = ", "
        return (
            input(
                f"select option for {key}, possible options are : {separator.join(opt)} : "
            )
            + " "
        )


print("Detecting OS type...")
_os = platform.system()
if _os == "Windows":
    print("ERROR: INSTALLATION on windows is work in progress")
    exit
    # print("Please use Windows Subsystem Linux(WSL) ")
    # print("Installation DONE!!")
else:

    cmake_def = ' -G "Ninja" -D CMAKE_BUILD_TYPE:STRING=Release'
    cmake_def += " -D BUILD_SHARED_LIBS:BOOL=ON "

    default_build_dir = "${HOME}/temp/easifem-extpkgs/Sparsekit/build"
    opt = getOption("Build directory: ", [f"{default_build_dir}", "build/dir/path"])

    if opt == " ":
        build_dir = default_build_dir

    print(f"Sparsekit will be build at {build_dir}")

    print("Enter the place where you want to install Sparsekit")
    opt = getOption("CMAKE_INSTALL_PREFIX: ", ["[${EASIFEM_EXTPKGS}], ${PREFIX}"])
    if opt == " ":
        opt = "${EASIFEM_EXTPKGS}"
    cmake_def += " -D CMAKE_INSTALL_PREFIX=" + opt
    print(f"Sparsekit will be installed at {opt}")

    print("Sparsekit is configured with : ", cmake_def)

    os.makedirs(build_dir, exist_ok=True)
    os.system(f"cmake -S ./ -B {build_dir} {cmake_def}")
    os.system(f"cmake --build {build_dir} --target install")
    print("Installation DONE!!")
