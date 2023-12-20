def _read_csv(path="questions.csv"):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        names = lines[0].split(',')
        data = [
            {
                name: value
                for name, value in
                zip(names, line.split(','))
            }
            for line in lines[1:]
        ]
        print(data)


_read_csv()
