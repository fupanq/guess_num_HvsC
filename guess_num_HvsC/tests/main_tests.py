from nose.tools import *
import NAME

def setup():
    print("setup!")
    pass

def teardown():
    print("teardown!")

def test_basic():
    print("I Ran!")

setup()
test_basic()
