all: build

build: clean
	gcc -o server server.c -no-pie -fno-stack-protector -z execstack

run: all
	./server 1500

clean:
	rm -f server