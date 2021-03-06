cmake_minimum_required(VERSION 3.13.0)
project(poker-cli VERSION 0.0.1 LANGUAGES CXX)

include(CTest)
enable_testing()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -O1 -g -fsanitize=address -fno-omit-frame-pointer")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -s -ffast-math -march=native -mtune=native")

find_program(TIDY "clang-tidy-11")
# set(CMAKE_CXX_CLANG_TIDY "${TIDY};-checks=-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},bugprone-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},cppcoreguidelines-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},clang-analyzer-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},misc-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},modernize-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},performance-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},portability-*")
# set(CMAKE_CXX_CLANG_TIDY "${CMAKE_CXX_CLANG_TIDY},readability-*")

include_directories(${CMAKE_CURRENT_LIST_DIR}
    ${CMAKE_CURRENT_LIST_DIR}/../include
    )

add_executable(poker-cli main.cpp)
#target_include_directories(poker-cli PRIVATE include)
target_link_libraries(poker-cli ${CONAN_LIBS} client api)
target_compile_options(poker-cli PRIVATE -Wall -Wextra)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -rdynamic")
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)