from models import Stack


balance_1 = Stack("(((([{}]))))")
balance_2 = Stack("[([])((([[[]]])))]{()}")
balance_3 = Stack("{{[()]}}")

imbalance_1 = Stack("}{}")
imbalance_2 = Stack("{{[(])]}}")
imbalance_3 = Stack("[{())}")

if __name__ == '__main__':
    print(balance_1.correct_incorrect())
    print(balance_2.correct_incorrect())
    print(balance_3.correct_incorrect())
    print(imbalance_1.correct_incorrect())
    print(imbalance_2.correct_incorrect())
    print(imbalance_3.correct_incorrect())

