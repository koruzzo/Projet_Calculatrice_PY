"""..."""
import os # pylint: disable=unused-import
import tkinter as tk # pylint: disable=unused-import
import pytest # pylint: disable=unused-import
import pandas as pd # pylint: disable=unused-import
from calculatrice import calc_and_err, replace_commas, save_operation, show_last_5, reset_entry # pylint: disable=unused-import

def test_replace_commas():
    """..."""
    assert replace_commas("9,1 + 4,5") == "9.1 + 4.5"
    assert replace_commas("9,1 + 4.5") == "9.1 + 4.5"
    assert replace_commas("3,14") == "3.14"
    assert replace_commas("6,27 * 2") == "6.27 * 2"




# def test_save_operation(tmp_path):
#     """..."""
#     operations_file = tmp_path / "operations.csv"
#     save_operation("1+2", 3)
#     assert os.path.exists(operations_file)
#     save_operation("3*4", 12)
#     data = pd.read_csv(operations_file)
#     assert len(data) == 2

# def test_reset_entry():
#     """..."""
#     root = tk.Tk()
#     entry = tk.Entry(root)
#     result_label = tk.Label(root)
#     reset_entry()
#     assert entry.get() == ""
#     assert result_label.cget("text") == "Résultat : "


# import variable
# import pytest


# def test_number_1_my_list():
#     """Check if my list is a list
#     """
#     assert(isinstance(variable.my_list, list))


# @pytest.mark.parametrize("number_1, number_2", [(2, 2), (3, 5), (6, 10)])
# def test_number_2_my_list_length(number_1, number_2):
    
#     computed_result = eval(f"{number_1}+{number_2}")
#     expected_result = number_1+number_2
    
#     assert(computed_result==expected_result)
    
    
