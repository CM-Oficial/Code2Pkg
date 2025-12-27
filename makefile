# Code2pkg Makefile
CC = clang
CFLAGS = -Wall -O2
# O nome do arquivo vem do comando que o c2p envia
SOURCE ?= main.c
TARGET = build/output.elf

all: $(TARGET)

$(TARGET): $(SOURCE)
	@mkdir -p build
	$(CC) $(CFLAGS) $(SOURCE) -o $(TARGET)
	@echo "Compilado: $(TARGET)"

clean:
	rm -rf build/
