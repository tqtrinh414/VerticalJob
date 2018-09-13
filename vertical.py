import pandas as pd

def read_dataframe(path = "verticals.csv"):
    df = pd.read_csv(path)
    df = df.drop(["status","creation_date","code","modification_date"],axis = 1)
    return df


def convert_df_dct(df):
    id_list = list(df["id"])
    parent_id_list = list(df["parent_id"])
    name_list = list(df["name"])
    dct = {}
    for i in range(0, len(id_list)):
        dct[id_list[i]] = (parent_id_list[i], name_list[i].lower())
    return dct


def path_id_list(dct, xid):
    path_list = []
    path_list.append(xid)
    parent_id = dct[xid][0]
    while (parent_id != 0):
        path_list.append(parent_id)
        parent_id = dct[parent_id][0]
    return path_list


def print_path(dct, xid):
    path_lst = path_id_list(dct, xid)
    for i in range(len(path_lst) - 1, -1, -1):
        print("->", dct[path_lst[i]][1], end = '')
    print("\n")


def processing(dct, s):
    s = s.lower()
    flag = 0
    for xid in dct:
        if dct[xid][1].find(s) != -1:
            flag = 1
            print_path(dct, xid)
    if flag == 0:
        print ("not found!!!")
        quit()

import time

def main():
    df = read_dataframe()
    dct = convert_df_dct(df)

    search = input("search: ")
    start = time.time()
    processing(dct, search)
    print ("----- search time:  ", time.time() - start, "-----")


if __name__ == "__main__":
    main()