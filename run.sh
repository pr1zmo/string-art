#!/bin/bash
g++ -c -fPIC *.cpp
g++ -shared -Wl,-soname,libfoo.so -o ./libfoo.so *.o
rm *.o