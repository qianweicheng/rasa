
if __name__ == '__main__':
    data = ''
    with open('./data/nlu_normal.md', 'r') as f:
        data = f.read()
        pass
    lower_data = data.lower()
    with open('./data/nlu_lower_case.md', 'w') as f:
        f.write(lower_data)
        pass

