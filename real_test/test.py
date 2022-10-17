def test(file):
    with open(file, encoding='utf8') as f:
        while True:
            one_line = f.readline()
            if not one_line:
                return
            yield one_line
