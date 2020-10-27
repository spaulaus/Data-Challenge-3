"""
Data investigation
"""
from uuid import uuid4
from os import listdir

from pandas import read_csv, set_option, DataFrame
from sklearn import decomposition

set_option('display.max_columns', None)

DATA_LABELS = ['unit', 'cycles', 'op_setting1', 'op_setting2', 'op_setting3', 's1', 's2', 's3',
               's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16',
               's17', 's18', 's19', 's20', 's21']


def main():
    data_base_dir = "Data"
    dataset_name = 'train'

    df = DataFrame()
    for file in [f for f in listdir(data_base_dir) if f.find(dataset_name) != -1]:
        tmp_df = read_csv(f"{data_base_dir}/{file}", delimiter=" ", names=DATA_LABELS,
                          usecols=range(len(DATA_LABELS)))
        for i in range(tmp_df.unit.max()):
            tmp_df.map()
        print(df)
        # df = df.append()
    # print(df.describe())

    is_last_measurement_index = df.groupby(['unit'])['cycles'].transform(max) == df['cycles']
    last_measured_df = df[is_last_measurement_index]
    penultimate_measured_df = df[df.index.isin([x - 1 for x in last_measured_df.index])]

    last_measured_df.to_csv("Data/temp-failure.csv")
    penultimate_measured_df.to_csv("Data/temp-before-failure.csv")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt caught, cleaning up.")
    finally:
        print("Exiting...")
