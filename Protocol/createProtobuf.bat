del /F /A /Q ./JS/*
del /F /A /Q ./Php/*
del /F /A /Q ./Python/*
del /F /A /Q ./Java/*

protoc.exe -I=./Protocol --python_out=./Python ./Protocol/game.proto
protoc.exe -I=./Protocol --java_out=./Java ./Protocol/game.proto
protoc.exe -I=./Protocol --php_out=./Php ./Protocol/game.proto
protoc.exe --js_out=library=game_pb,binary:./JS ./Protocol/game.proto

copy Python\game_pb2.py ..\server\protocol

echo "build proto success!"