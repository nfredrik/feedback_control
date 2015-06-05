import types

def public(func):
  def wrapper(self,*__args,**__kw):
    self.checkRep() # check before executing
    res = func(self,*__args,**__kw)
    self.checkRep() # check after executing
    return res
  return wrapper

def constructor(func):
  def wrapper(self,*__args,**__kw):
    func(self,*__args,**__kw)
    self.checkRep() # check after executing constructor
  return wrapper

# Put "__metaclass__ = EnforceCheckRep" inside a class declaration to
# have it automatically decorate its constructor and public methods with
# checkRep() calls
def EnforceCheckRep(name, bases, attrs):
  print("called!")
  for k in attrs:
    if k == '__init__':
      attrs[k] = constructor(attrs[k])
    # ignore private methods that start with '_' (and of course ignore checkRep itself)
    elif k[0] != '_' and k != 'checkRep':
      f = attrs[k]
      if isinstance(f, types.FunctionType):
        attrs[k] = public(f)
  return type(name, bases, attrs)
  
