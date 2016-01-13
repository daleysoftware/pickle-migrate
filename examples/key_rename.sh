#!/bin/bash
set -eu
cd $(dirname $0)
cp key_rename.db /tmp
../env/bin/python key_rename.py /tmp/key_rename.db
rm /tmp/key_rename.db
