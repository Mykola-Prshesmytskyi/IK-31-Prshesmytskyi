import logging
def my_def(A):
        for k in range(100):
            if A:
                if k % 2 == 0:
                    print(k)
            else:
                if k % 2 != 0:
                    print(k)


#### Функція з помилкою

def eror(x,y):
    try:
        z = x+y
        return z
        logging.info("Без помилок")
    except Exception as e:
        logging.error(e)
