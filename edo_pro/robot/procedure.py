def p1(a, b):
    print("test1")
    return True


def p2(a, b):
    print("test2")
    return False


if __name__ == "__main__":
    p1("str1", "str2")
    p2("str3", "str4")