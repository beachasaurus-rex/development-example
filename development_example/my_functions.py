# This function returns True if `num_to_compare` is near `reference`, within the specified tolerance `tol`.
def is_near_number(num_to_compare, reference, tol):
    rel_diff = 0
    if reference == 0:
        rel_diff = num_to_compare - reference
    else:
        rel_diff = (num_to_compare - reference) / reference
    return rel_diff >= -tol and rel_diff <= tol
