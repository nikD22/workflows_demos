import main

def test_add():
  assert main.add(2, 3) == 5
  assert main.add(-1, 1) == 0
  assert main.add(0, 0) == 0
  assert main.add(0,0) ==1


def test_subtract():
  assert main.subtract(5, 3) == 2
  assert main.subtract(0, 4) == -4
  assert main.subtract(-2, -2) == 0


def test_divide():
  assert main.divide(6, 3) == 2
  assert main.divide(5, 2) == 2.5
