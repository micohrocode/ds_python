class Doubler:
    def __init__(self, n):
        self._n = 2 * n
    
    def n(self):
        return self._n
    
if __name__ == '__main__':
    x = Doubler(5)
    # test that is it true
    # error if it isnt
    assert(x.n()==10)
    y = Doubler(-4)
    assert(y.n()==-8)