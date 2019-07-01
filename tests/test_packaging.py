""" Validate what's available directly on the top-level import. """

import pytest
from inspect import isfunction

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


@pytest.mark.parametrize(["obj_name", "typecheck"], [
    ("check_all_commands", isfunction), ("determine_uncallable", isfunction)])
def test_top_level_exports(obj_name, typecheck):
    """ At package level, validate object availability and type. """
    import pypiper
    try:
        obj = getattr(pypiper, obj_name)
    except AttributeError:
        pytest.fail("Unavailable on {}: {}".format(pypiper.__name__, obj_name))
    else:
        assert typecheck(obj)
