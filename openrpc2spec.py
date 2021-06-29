#!/usr/bin/env python3

import json
import sys

openrpc = json.load(sys.stdin)

def openrpc2example(obj, default):
    if 'schema' not in obj:
        return default
    if 'examples' not in obj['schema']:
        return {}
    result = obj['schema']['examples'][0]
    if result is None:
        return default
    return result

spec = []
for method in openrpc['methods']:
    method = {
        'name': method['name'],
        'params': [openrpc2example(param, {}) for param in method['params']],
        'returns': openrpc2example(method['result'], None)
    }
    if method['returns'] is None:
        del method['returns']
    spec.append(method)

json.dump(spec, sys.stdout, indent=2)
