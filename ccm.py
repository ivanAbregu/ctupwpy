class CustomCM():
    def __init__(self):
        self.enter = 1

    def __enter__(self):
        print('****' * self.enter)
        self.enter+=1
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.enter -=1
        print('****' * self.enter)


if __name__ == '__main__':
    with CustomCM() as cm:
        with cm as cm:
            with cm as cm:
                pass