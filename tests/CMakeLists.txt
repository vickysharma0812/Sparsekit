cmake_minimum_required(VERSION 3.14.0 FATAL_ERROR)
set(PROJECT_NAME "Sparsekit")
project(${PROJECT_NAME})
enable_language(Fortran)

# if cmake_predix_path is not defined then we take value of
# EASIFEM_EXTPKGS
if(NOT CMAKE_PREFIX_PATH)
  set(CMAKE_PREFIX_PATH "$ENV{EASIFEM_EXTPKGS}")
endif()

add_executable(test_${PROJECT_NAME})
target_sources(
  test_${PROJECT_NAME}
  PRIVATE
  test_${PROJECT_NAME}.f90
)

find_package(${PROJECT_NAME} 1 CONFIG REQUIRED)

if(${PROJECT_NAME}_FOUND)
  message(STATUS "Found ${PROJECT_NAME}")
  target_link_libraries(
    test_${PROJECT_NAME}
    PRIVATE
    ${PROJECT_NAME}::${PROJECT_NAME}
  )
else()
  message("FATAL ERROR: project not found")
endif()
