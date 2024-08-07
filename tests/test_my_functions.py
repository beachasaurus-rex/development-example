from numpy import arange
from pytest import mark

from my_functions import is_near_number


@mark.parametrize(
    "name,test_vals,ref_val,tol",
    [
        ["1--step_1e-7", arange(1 - (1e-6 * (1 - 0.01)), 1 + 1e-6, 1e-7), 1, 1e-6],
        ["0--step_1e-7", arange(-1e-6, 1e-6, 1e-7), 0, 1e-6],
    ],
)
def test_is_near_number(name, test_vals, ref_val, tol):
    for i in range(0, len(test_vals)):
        assert is_near_number(test_vals[i], ref_val, tol)
