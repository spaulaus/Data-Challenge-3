"""
Data investigation
"""

from pandas import read_csv

DATA_LABELS = ['unit', 'cycles', 'op_setting1', 'op_setting2', 'op_setting3', 's1', 's2', 's3',
               's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16',
               's17', 's18', 's19', 's20', 's21']

TEST_FILES: [
    "Data/test_FD001.txt",
    "Data/test_FD002.txt",
    "Data/test_FD003.txt",
    "Data/test_FD004.txt"
]


def main():
    for filename in TEST_FILES:
        df = read_csv(filename, index_col=None, header=0)
        li.append(df)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt caught, cleaning up.")
    finally:
        print("Exiting...")
