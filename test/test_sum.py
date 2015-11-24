#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from listcounts import sum


@raises(TypeError)
def test_sum_takes_a_list_as_argument():

    sum(30)

#@raises(ValueError)
#def test_sum_takes_a_non_empty_list_as_argument():

    sum([3])
#

def test_sum_a_list_with_3_7_5_should_give_15():

    assert_equal(sum([3, 7, 5]), 15)


def test_sum_a_list_with_3_should_give_3():

    assert_equal(sum([3]), 3)