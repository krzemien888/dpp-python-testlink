#!/usr/bin/env bash

export TESTLINK_API_PYTHON_SERVER_URL=http://192.168.100.100/lib/api/xmlrpc/v1/xmlrpc.php
export TESTLINK_API_PYTHON_DEVKEY=74ca1b065b0e8466e4536f39a8215284

python3 test_connection.py
