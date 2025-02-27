def sort(width: float, height: float, length: float, mass: float) -> str:
  """
  Sorts a package into the correct stack with respect to its dimensions and mass.

  :param width: The width of the package in centimeters. must be > 0
  :param height: The height of the package in centimeters. must be > 0
  :param length: The length of the package in centimeters. must be > 0
  :param mass: The mass of the package in centimeters. must be >= 0
  :return: "STANDARD", "SPECIAL" or "REJECTED".

  :raises TypeError: If inputs are non-numeric or boolean.
  :raises ValueError: If dimensions are <= 0  or mass < 0.
  """

  for val in [width, height, length, mass]:
    if isinstance(val, bool):
      raise TypeError("Boolean values are not allowed for dimensions or mass.")
    if not isinstance(val, (int, float)):
      raise TypeError("All inputs must be int or float.")

  #Check for valid numeric ranges
  if width <= 0 or height <= 0 or length <= 0:
    raise ValueError("All dimensions must be greater than 0.")
  if mass < 0:
    raise ValueError("Mass cannot be negative.")

  #Safe volume calculation
  try:
    volume = width * height * length
  except Exception as e:
    raise ValueError("Error calculating volume.") from e

  #Classification flags
  is_bulky = (volume >= 1_000_000) or (width >= 150 or height >= 150
                                       or length >= 150)
  is_heavy = (mass >= 20)

  #Determine stack
  if is_bulky and is_heavy:
    return "REJECTED"
  elif is_bulky or is_heavy:
    return "SPECIAL"
  else:
    return "STANDARD"
