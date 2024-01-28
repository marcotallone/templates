# Setting the name for the C++ library
set(LIBRARY_NAME your_cpp_library_name) # <--- CHANGE THIS

# Setting the name for the Python module
set(MODULE_NAME your_python_module_name) # <--- CHANGE THIS

# Setting the list of source files
set(SOURCE_FILES 
    # source1.cpp # <--- ADD YOUR SOURCE FILE HERE
    # source2.cpp # <--- ADD YOUR SOURCE FILE HERE
)

# Setting lib directory
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Verifying third party libraries installation # <--- UNCOMMENT THIS SECTION AND CHANGE THE NAME OF THE LIBRARY IF NEEDED
# find_package(library_name REQUIRED)
# if(library_name_FOUND)
#     message("✅ library_name Library Found")
# 	message(STATUS "🔎  Checking library_name_LIBRARIES: ${library_name_LIBRARIES}")
# 	message(STATUS "🔎  Checking library_name_INCLUDE_DIRS: ${library_name_INCLUDE_DIRS}")
# else()
    # message(FATAL_ERROR "⚠️  library_name Library Not Found: Please install it in order to continue")
# endif()

find_package(pybind11 REQUIRED)
if(pybind11_FOUND)
    message("✅ Pybind11 Library Found")
else()
    message(FATAL_ERROR "⚠️  Pybind11 Library Not Found: Please install it in order to continue")
endif()

# Including directories
set(INCLUDE_DIRS 
	${CMAKE_SOURCE_DIR}/include 
    # ${source_directory_of_third_library}
    SYSTEM ${pybind11_INCLUDE_DIRS})

include_directories(${INCLUDE_DIRS})

# Compiling C++ libraries
add_library(${LIBRARY_NAME} SHARED ${SOURCE_FILES})

# Setting library version
set_target_properties(${LIBRARY_NAME} PROPERTIES VERSION 1.0.0 SOVERSION 1)

# Linking libraries
# target_link_libraries(${LIBRARY_NAME} ${third_library_name_LIBRARIES}) # <--- UNCOMMENT THIS LINE AND CHANGE THE NAME OF THE LIBRARY IF NEEDED

# Compiling and linking Python bindings
pybind11_add_module(${MODULE_NAME} MODULE ${SOURCE_FILES})
target_link_libraries(${MODULE_NAME} PRIVATE ${LIBRARY_NAME})
