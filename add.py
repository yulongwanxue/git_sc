def add(a, b):
    """
    计算两个数的和

    参数:
        a: 第一个数
        b: 第二个数

    返回:
        两个数的和
    """
    return a + b


if __name__ == "__main__":
    # 测试函数
    result = add(5, 3)
    print(f"5 + 3 = {result}")

    result = add(10.5, 20.3)
    print(f"10.5 + 20.3 = {result}")
