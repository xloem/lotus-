cmake_minimum_required(VERSION 3.6)

project(lotus++)

find_package(PkgConfig REQUIRED)
pkg_check_modules(libjson-rpc-cpp REQUIRED IMPORTED_TARGET
	libjsonrpccpp-client libjsonrpccpp-common)
#find_package(libjson-rpc-cpp REQUIRED IMPORT)
find_program(libjson-rpc-cpp_STUBTOOL jsonrpcstub REQUIRED)

add_library(lotus++ INTERFACE lotus.hpp)

add_custom_command(
	OUTPUT lotus.json
	DEPENDS openrpc2spec.py
	COMMAND zcat lotus.json.gz | python3 openrpc2spec.py
)
add_custom_command(
	OUTPUT lotus.hpp
	DEPENDS lotus.json PkgConfig::libjson-rpc-cpp
	COMMAND $(libjson-rpc-cpp_STUBTOOL) lotus.json --cpp-client=lotus::Filecoin --cpp-client-file=lotus.hpp.tmp
	COMMAND sed 's/nullValue/arrayValue/' -i lotus.hpp.tmp
	COMMAND sed 's/Filecoin_//' -i lotus.h.tmp
	mv lotus.hpp.tmp lotus.hpp
)

install(FILES lotus.hpp DESTINATION include)

#target_sources(lotus++ INTERFACE lotus.hpp)

target_link_libraries(lotus++ PkgConfig::libjson-rpc-cpp)#libjson-rpc-cpp::jsonrpccommon libjson-rpc-cpp::jsonrpcclient)


add_executable(example example.cpp)
target_link_libraries(example lotus++)
