#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from listcounts import min




@raises(TypeError)
def test_min_takes_a_list_as_argument():

    min()

@raises(ValueError)
def test_min_takes_a_non_empty_list_as_argument():

    min([])


def test_min_a_list_with_3_5_7_should_give_3():

    assert_equal(min([3, 5, 7]), 3)


def test_min_a_list_with_9_3_5_2_should_give_2():

    assert_equal(min([9, 3, 5, 2]), 2)


def test_min_a_list_with_3_5_should_give_3():

    assert_equal(min([3, 5]), 3)


def test_min_a_list_with_3_should_give_():

    assert_equal(min([3]), 3)