def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def divide(a, b):
  return a / b

def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  assert add(0, 0) == 0


def test_subtract():
  assert subtract(5, 3) == 2
  assert subtract(0, 4) == -4
  assert subtract(-2, -2) == 0


def test_divide():
  assert divide(6, 3) == 2
  assert divide(5, 2) == 2.5
