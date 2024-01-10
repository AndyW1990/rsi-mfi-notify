

##################### TESTS #####################
test_vals:
	@pytest \
	tests/test_vals.py::TestVals::test_buy \
	tests/test_vals.py::TestVals::test_sell \
	tests/test_vals.py::TestVals::test_do_nothing_1 \
	tests/test_vals.py::TestVals::test_do_nothing_2 \
	tests/test_vals.py::TestVals::test_do_nothing_3