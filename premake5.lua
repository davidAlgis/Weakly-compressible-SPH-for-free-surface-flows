---------------------------------
-- [ WORKSPACE CONFIGURATION   --
---------------------------------
workspace "WCSPH"
language "C++"
cppdialect "C++17"
configurations { "Debug", "Release" } -- Optimization/General config mode in VS
platforms { "x64" } -- Dropdown platforms section in VS
-------------------------------
-- [ COMPILER/LINKER CONFIG] --
-------------------------------
-- Here we are setting up what differentiates the configurations that we called "Debug" and "Release"
filter "configurations:Debug"
defines { "DEBUG" }
symbols "On"
warnings "Extra"
filter "configurations:Release"
defines { "NDEBUG" }
optimize "On"
warnings "Extra"
filter { "platforms:*64" }
architecture "x64"
filter { "action:gmake" }
filter { "system:macosx", "action:gmake" }
toolset "clang"
filter {}


project "WCSPH"
location("./")
targetdir("./bin/")
local tempDir = "./temp/"
objdir(tempDir)
kind "ConsoleApp"
local sourceDir = "./src/";
files
{
   sourceDir .. "**.cpp",
}
includedirs
{
   "./freeglut/include"
}
libdirs
{
   ".\\freeglut/build/bin/Release/",
   ".\\freeglut/build/bin/Debug/",
   ".\\freeglut/build/lib/Release/",
   ".\\freeglut/build/lib/Debug/",
}
links { "OpenGL32", "freeglut", "freeglutd" }
