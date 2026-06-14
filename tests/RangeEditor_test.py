import holypython
import utils

def test_edit_literal_range():
	namespace = utils.run_source(holypython.RangeEditor, "result = list([1..3])")
	assert namespace["result"] == [1, 2, 3]

def test_edit_range_call():
	source = holypython.RangeEditor("print_receipt([1..5])").edit_source()
	assert source == "print_receipt(list(range(1, 5 + 1)))"

def test_edit_range_function_endpoints():
	source = """
def f(x):
	return x + 1

def g(y):
	return y + 2

result = [f(1)..g(2)]
"""
	namespace = utils.run_source(holypython.RangeEditor, source)
	assert namespace["result"] == [2, 3, 4]

def test_edit_range_function_endpoint_with_range_argument():
	source = """
def generate_random_day_of_week_as_integer(days):
	return days[0]

result = [generate_random_day_of_week_as_integer([1..7])..10]
"""
	namespace = utils.run_source(holypython.RangeEditor, source)
	assert namespace["result"] == list(range(1, 11))

def test_edit_range_in_list():
	source = """
def generate_random_day_of_week_as_integer(days):
	return days[-1]

result = [generate_random_day_of_week_as_integer([1..7]), 10]
"""
	namespace = utils.run_source(holypython.RangeEditor, source)
	assert namespace["result"] == [7, 10]

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
