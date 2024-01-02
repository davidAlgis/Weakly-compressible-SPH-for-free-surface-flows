import os
import platform
import subprocess
import shutil


def main():
    # Check for Operating System
    os_name = platform.system()

    # Initialize and update the FreeGLUT submodule
    os.system("git submodule init")
    os.system("git submodule update")

    # Navigate into the FreeGLUT directory
    os.chdir("freeglut")

    # Create a build directory and navigate into it
    if not os.path.exists("build"):
        os.makedirs("build")
    os.chdir("build")

    configure_cmd = "cmake .. -D CMAKE_BUILD_TYPE=Release"

    # Configure and Generate the Makefile
    print("Configuring with CMake...")
    configure_result = os.system(configure_cmd)

    if configure_result != 0:
        print("Configuration failed. Please check the CMake configuration.")
        return

    build_cmd = "cmake --build .  --config Release"
    print("Building with CMake...")
    build_result = os.system(build_cmd)
    if build_result != 0:
        print("Build failed. Please check the build configuration.")
        return
    print("Build successful.")

    # Define the source and destination paths
    source_dll = "./bin/Release/freeglut.dll"
    dest_folder = "../../bin"
    # Check if the DLL exists
    if not os.path.exists(source_dll):
        print("The freeglut.dll does not exist. Ensure the build was successful and the path is correct.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Copy the file
    shutil.copy(source_dll, dest_folder)
    print("Copied freeglut.dll to binary folder")


if __name__ == "__main__":
    main()
