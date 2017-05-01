#!/usr/bin/env bash

LOOM_HOST="http://localhost:7000"

curl -v \
     -X POST \
     -d @loom/model.json \
     ${LOOM_HOST}/models

curl -v \
     -X POST \
     -d @loom/fabric.json \
     ${LOOM_HOST}/fabrics

