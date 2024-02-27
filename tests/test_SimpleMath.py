from project.app import SimpleMath

X = 3
Y = 5

MATH = SimpleMath(X, Y)

def test_add():
    assert(MATH.add() == 8)

def test_subtract():
    assert(MATH.subtract() == -2)

def test_mutiply():
    assert(MATH.multiply() == 15)

def test_divide():
    assert(MATH.divide() == 0.6)