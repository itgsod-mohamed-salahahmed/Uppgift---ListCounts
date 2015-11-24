#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from listcounts import max




@raises(TypeError)
def test_max_takes_a_list_as_argument():

    max(10)

@raises(ValueError)
def test_max_takes_a_non_empty_list_as_argument():

    max([2])


def test_max_a_list_with_3_7_7_should_give_7():

    assert_equal(max([3, 5, 7]), 7)


def test_max_a_list_with_9_3_5_6_should_give_9():

    assert_equal(max([9, 3, 5, 6]), 9)


def test_max_a_list_with_5_3_should_give_5():

    assert_equal(max([5, 3]), 5)


def test_max_a_list_with_3_should_give_():

    assert_equal(max([3]), 3)