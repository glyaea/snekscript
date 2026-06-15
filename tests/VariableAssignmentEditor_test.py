import holypython
import utils

def test_edit_assignment():
	namespace = utils.run_source(holypython.VariableAssignmentEditor, "result <- 37")
	assert namespace["result"] == 37

def test_keep_comparison():
	namespace = utils.run_source(holypython.VariableAssignmentEditor, "result = 1 < -2")
	assert namespace["result"] is False
