import divisor_master

def test_prime():
  assert prime('668 431 386 107 93') == [431, 107]
   
def test_prime_2():
  assert prime('423 974 836 474 428 142') == []

def test_divider():
  assert divider('668') == {668: [1, 2, 4, 167, 334, 668]}

def test_divider_2():
  assert divider('123 268') == {123: [1, 3, 41, 123], 268: [1, 2, 4, 67, 134, 268]}
  
def test_prime_dividers():
  assert prime_dividers('668') == {668: 167}
  

