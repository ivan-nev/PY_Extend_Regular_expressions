import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import pandas as pd
import numpy


if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter="\n")
        contacts_list = list(rows)


    #  выполните пункты 1-3 ДЗ
    contacts_list_good = []

    pat_tel = r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})(\s)*\(*(доб.)*\.*\s*(\d+)*\)*'
    sub_tel = r'+7(\2)\3-\4-\5\6\7\8'
    pat_fio = r'([A-Я][а-я]+)\s([A-Я][А-я]+)\s([А-я]+)(,)(,)(,)'
    sub_fio = r'\1\4\2\5\3\6'
    pat_fio2 = r'([A-Я][а-я]+)\s([A-Я][А-я]+)(,)(,)'
    sub_fio2 = r'\1\3\2\4'
    for contact in contacts_list:
        result = re.sub(pat_tel, sub_tel, contact[0])
        result = re.sub(pat_fio, sub_fio, result)
        result = [re.sub(pat_fio2, sub_fio2, result)]
        res2 = result[0].split(',')
        contacts_list_good.append(res2)
    # pprint(contacts_list_good)
    df = pd.DataFrame(contacts_list_good, columns=contacts_list_good[0])
    df.drop(labels=[0], axis=0, inplace=True) #удаляет 0 строку т.к в ней названия колонок
    pprint(df)
    dz = df.groupby(['lastname', 'firstname'])[
        ['lastname', 'firstname','surname','organization','position','phone','email']].max()
    # https://datagy.io/pandas-groupby/
    pprint(dz)
    dz.to_csv('phonebook.csv', index=False)





    #  сохраните получившиеся данные в другой файл
    # # код для записи файла в формате CSV
    # with open("phonebook.csv", "w", encoding='utf-8') as f:
    #     datawriter = csv.writer(f, lineterminator="\n" )
    #     # Вместо contacts_list подставьте свой список
    #     datawriter.writerows(contacts_list_good)

    # data = pd.read_csv('phonebook.csv')
    # # print(data.head(3))
    # pprint(data.columns.tolist())
    # # data.to_csv('123.csv', index=False)
    # # # dy = data.duplicated(subset=['brand','style'])
    # # # print(dy)

