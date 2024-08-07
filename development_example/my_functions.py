# This function returns the relative difference between `reference` and `num_to_compare`.
def rel_diff(num_to_compare, reference):
    if reference == 0:
        return num_to_compare - reference
    else:
        return (num_to_compare - reference) / reference


# This function returns True if `num_to_compare` is near `reference`, within the specified tolerance `tol`.
def is_near_number(num_to_compare, reference, tol):
    err = abs(rel_diff(num_to_compare, reference))
    return err <= tol
