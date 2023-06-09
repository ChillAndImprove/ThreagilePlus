build:
	GOOS=js GOARCH=wasm go build -o main.wasm

move:
	cp main.wasm ../../www/
    
all: build move

