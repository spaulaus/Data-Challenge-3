"""
Data investigation
"""

from pandas import read_csv, set_option

set_option('display.max_columns', None)

DATA_LABELS = ['unit', 'cycles', 'op_setting1', 'op_setting2', 'op_setting3', 's1', 's2', 's3',
               's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16',
               's17', 's18', 's19', 's20', 's21']


def generate_data_set_name(dataset_type, dataset_number):
    return f'Data/{dataset_type}_FD00{dataset_number}.txt'


def main():
    dataset_name = 'train'
    dataset_number = 1
    df = read_csv(generate_data_set_name(dataset_name, dataset_number),
                  delimiter=" ", names=DATA_LABELS, usecols=range(len(DATA_LABELS)))

    is_last_measurement_index = df.groupby(['unit'])['cycles'].transform(max) == df['cycles']
    last_measured_df = df[is_last_measurement_index]
    print(last_measured_df)

    penultimate_measured_df = df[df.index.isin([x - 1 for x in last_measured_df.index])]
    print(penultimate_measured_df)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt caught, cleaning up.")
    finally:
        print("Exiting...")
