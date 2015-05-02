swig -c++ -python example.i
g++ -c *.cpp *.cxx -I/usr/include/python2.7 -fPIC
g++ -shared example.o example_wrap.o -o _example.so
