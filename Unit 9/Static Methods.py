class Fraction:
      
  def __init__ (self, n, d):
    if d < 0:
      self.__num = -n
      self.__den = -d
    else:
      self.__num = n
      self.__den = d
      
  def times(self, other):
    result = Fraction(self.__num*other.__num,self.__den*other.__den)
    return result
    
  @staticmethod # function decorator
  def product(f1,f2):
    result = Fraction(f1.__num*f2.__num,f1.__den*f2.__den)
    return result