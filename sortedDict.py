if __name__ == '__main__':
    markdict = {"Tom": 67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya": 73}
    sortdict = dict(
        sorted(markdict.items(), key=lambda x: x[1], reverse=False))
    print(sortdict)
