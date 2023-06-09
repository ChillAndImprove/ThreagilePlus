build:
	GOOS=js GOARCH=wasm go build -o main.wasm

move:
	cp main.wasm visual/maxgraph/javascript/examples/grapheditor/www/
    
all: build move

