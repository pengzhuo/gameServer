#!/usr/bin/env bash
rm -rf ./JS/*
rm -rf ./Php/*
rm -rf ./Python/*

protoc -I=./Protocol --python_out=./Python ./Protocol/game.proto
protoc -I=./Protocol --java_out=./Java ./Protocol/game.proto
protoc -I=./Protocol --php_out=./Php ./Protocol/game.proto
protoc --js_out=library=game_pb,binary:./JS ./Protocol/game.proto

cp ./Python/game_pb2.py ../server/protocol

echo "生成成功"