import pytest

from arquivo import soma, menos, this_num

def test_xyz():
	assert soma(4,4) == 8
	assert soma(5,5) == 10
	assert soma(2.4, 3.1) == 5.5
	assert soma( -2, -10) == -12

def test_usandostring():

	assert soma('-8', '-4') == 12
	assert soma('xyz',1) == None

def test_menos():
	assert menos(5,5) == 0
