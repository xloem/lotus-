#include <iostream>

#include "Filecoin.hpp"
#include <jsonrpccpp/client/connectors/httpclient.h>

using namespace jsonrpc;
using namespace std;
using namespace lotus;

int main()
{
	HttpClient httpclient("https://api.node.glif.io/rpc/v0");
	Filecoin filecoin(httpclient, JSONRPC_CLIENT_V2);

	Json::Value chainhead = filecoin.ChainHead();
	cout << chainhead << endl;
}
