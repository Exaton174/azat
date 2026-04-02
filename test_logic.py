

def add(a, b):
    return  a + b


def test_add_succes():
    assert add(2, 3) == 5


def test_add_wrong():
    assert add(2, 2) == 5


def get_user_number():
    try:
        num = int(input("Введите число "))
     
    except ValueError:
        print("Ошибка! Пажалуйста, введите только число, а не буквы.")

if __name__ == "__main__":
    get_user_number()




