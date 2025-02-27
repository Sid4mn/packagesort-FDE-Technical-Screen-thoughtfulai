import pytest
from main import sort

@pytest.mark.parametrize(
    "width, height, length, mass, expected",
    [
      (10, 10, 10, 1, "STANDARD"),
      (150, 10, 10, 10, "SPECIAL"), # Bulky
      (10, 10, 10, 20, "SPECIAL"), # Heavy
      (200, 200, 200, 30, "REJECTED"), # Both bulky & heavy
      (300, 10, 10, 1, "SPECIAL"), # Bukly, not heavy
      (10, 10, 10, 19.99, "STANDARD") # neither bulky or heavy
    ], ids=["small_STANDARD",
            "wide_bulky_SPECIAL",
            "heavy_SPECIAL",
            "both_heavy_bulky_REJECTED",
            "bulky_not_heavy_SPECIAL",
            "borderline_STANDARD"
    ])

def test_sort_valid_inputs(width, height, length, mass, expected):
  """
  Test standard inputs to ensure correct classification.
  """
  assert sort(width, height, length, mass) == expected

def test_sort_type_errors():
  """
  Test that TypeError is raised for non-numeric or boolean inputs.
  """
  with pytest.raises(TypeError):
    sort("100", 10, 10, 12) #string dimension
  with pytest.raises(TypeError):
    sort(10, None, 10, 12) #None dimension
  with pytest.raises(TypeError):
    sort(True, 10, 10, 12) #boolean dimension

def test_sort_value_errors():
  """
  Test that ValueError is raised for invalid inputs.(zero/negative).
  """
  with pytest.raises(ValueError):
    sort(-1, 10, 10, 12) # negative dimension
  with pytest.raises(ValueError):
    sort(10, 0, 10, 12) #zero dimension
  with pytest.raises(ValueError):
    sort(9, 10, 10, -12) #negative mass