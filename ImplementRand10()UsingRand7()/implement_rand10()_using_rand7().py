def rand10():
    while True:
        num = (rand7() - 1) * 7 + rand7()
        if num <= 40:
            return (num - 1) % 10 + 1