import holypython
import utils

def test_edit_literal_range():
	namespace = utils.run_source(holypython.RangeEditor, "result = list([1..3])")
	assert namespace["result"] == [1, 2, 3]

def test_edit_range_list():
	namespace = utils.run_source(holypython.RangeEditor, "result = [1..3]")
	assert namespace["result"] == [1, 2, 3]

def test_edit_variable_range():
	namespace = utils.run_source(holypython.RangeEditor, """
a = 2
b = 5
result = list([a..b])
""")
	assert namespace["result"] == [2, 3, 4, 5]
