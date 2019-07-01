from urllib import urlopen
shakespeare_poem = 'http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt'

poem = urlopen(shakespeare_poem)

print poem
