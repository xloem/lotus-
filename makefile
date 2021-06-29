example: example.cpp Filecoin.hpp
	g++ $< -ljsoncpp -lcurl -ljsonrpccpp-common -ljsonrpccpp-client -o $@

%.hpp: %.json
	jsonrpcstub $^ --cpp-client=lotus::$* --cpp-client-file=$@.tmp
	sed 's/nullValue/arrayValue/' -i $@.tmp 
	sed 's/Filecoin_//' -i $@.tmp
	mv $@.tmp $@

%.json: %.json.gz openrpc2spec.py
	zcat $< | python3 openrpc2spec.py > $@
