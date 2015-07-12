#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. $DIR/setEnv.sh

python -m proteomics.scripts.digest_and_ingest $@
