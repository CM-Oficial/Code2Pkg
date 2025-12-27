CC = clang
CFLAGS = -target powerpc-unknown-freebsd -m32 -march=pwr4 -O2
LDFLAGS = -nostdlib

all: pkg_root/USRDIR/EBOOT.BIN

pkg_root/USRDIR/EBOOT.BIN: build/output.elf
	python3 ../core/eboot_gen.py build/output.elf pkg_root/USRDIR/EBOOT.BIN

build/output.elf: src/main.c
	mkdir -p build
	$(CC) $(CFLAGS) $(LDFLAGS) src/main.c -o build/output.elf