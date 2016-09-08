cmake_minimum_required (VERSION 2.6)
project (fpmtop)

add_subdirectory(pugixml/ pugixml)
#add_definitions(${PUGIXML_DEFINITIONS})
include_directories(pugixml/src)
#link_directories(${PUGIXML_LIBRARY_DIRS})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")
#set(CMAKE_CXX_STANDARD 11) # C++11...
#set(CMAKE_CXX_STANDARD_REQUIRED ON) #...is required...
#set(CMAKE_CXX_EXTENSIONS OFF) #...without compiler extensions like gnu++11

file(GLOB all_SRC
    "src/*.h"
    "src/*.cpp"
)
add_executable(fpmtop ${all_SRC})

if (WIN32) #disable console mode for VC++
	set_target_properties(fpmtop PROPERTIES WIN32_EXECUTABLE TRUE)
endif(WIN32)

link_directories(/usr/lib/x86_64-linux-gnu /usr/lib64 /lib64)
target_link_libraries(fpmtop ncurses curl pugixml tinfo)
