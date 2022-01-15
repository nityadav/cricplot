import argparse
import json
import seaborn as sns
import matplotlib.pyplot as plt
import re


def str_to_int(string):
    string = re.sub("[^0-9]", "", str(string))
    return int(string) if string.strip() else 0


def get_innings_data():
    with open('test_innings.json') as innings_f:
        json_data = json.load(innings_f)
        name2inns = {j['name']: [str_to_int(i) for i in j['test_innings']] for j in json_data}
        return name2inns


def main(args):
    innings_data = get_innings_data()
    # players = {"Joe Root", "SPD Smith", "Virat Kohli", "Kane Williamson"}
    # innings_data = {k: v for k, v in innings_data.items() if k in players}
    # sns.kdeplot(data=innings_data)
    y = innings_data['SPD Smith']
    x = list(range(len(y)))
    sns.kdeplot(x=x, y=y)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('foo')
    # parser.add_argument('-b', '--bar')
    # parser.add_argument('-f', action='store_true')
    # parser.add_argument('-d', type=int, default='default_value')
    # parser.add_argument('-c', default='alice', choices=['alice', 'bob'])
    main(parser.parse_args())
