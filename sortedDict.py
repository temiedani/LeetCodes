if __name__ == '__main__':
    markdict = {"Tom": 67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya": 73}
    sortdict = dict(
        sorted(markdict.items(), key=lambda kv: kv[1], reverse=False))
    print(sortdict)

    score = [5, 4, 3, 11, 2, 1, 77]
    my_dict = {i: v for i, v in enumerate(score)}
    my_dict_sorted = dict(sorted(my_dict.items(), key=lambda xv: xv[0]))
