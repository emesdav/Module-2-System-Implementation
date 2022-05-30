class Validate:
  def ifInt(value):
    if value is not None:
      return isinstance(value, int)

  def ifString(value):
    if value is not None:
      return isinstance(value, str)

  def ifFloat(value):
    if value is not None:
      return isinstance(value, float)
  
