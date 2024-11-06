CC=gcc
CFLAGS=-g -Wall -Werror -pedantic -std=gnu99 -I./lib
LDFLAGS=-L. -Wl,-rpath,.
TARGET=etovucca
SRCDIR=src
LIBDIR=lib
DEPS=Database.o libsqlite3.so

.PHONY: all clean initdb cgi init-admin-db

all: $(TARGET)

cgi: etovucca
		python3 -m http.server --cgi

etovucca: $(DEPS) $(SRCDIR)/RTBB.c
		$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ -lsqlite3

Database.o: $(SRCDIR)/Database.c
		$(CC) $(CFLAGS) -o $@ -c $^

libsqlite3.so: $(LIBDIR)/sqlite3.c
		$(CC) -shared -o $@ -fPIC $^ -ldl -pthread
		$(CC) -o sqlite3 $^ $(LIBDIR)/shell.c -ldl -pthread

clean:
		$(RM) $(TARGET) $(DEPS) sqlite3 *.o admin.sqlite3

initdb: init-admin-db
		echo .quit | ./sqlite3 -init setup.sql rtbb.sqlite3

init-admin-db:
		echo .quit | ./sqlite3 -init admin_setup.sql admin.sqlite3
