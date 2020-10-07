'''

* 仕様 : DB作成
* 完成形 : {01:moji, 02:moji, ...} 
 
* 仕様 : 数字に対応する文字列を表示するアプリケーション制作
* 完成形 : 数字欄に文字列を入力すると正解か不正解か表示する

'''

import csv
import itertools
import pickle

from time import sleep

def setup_csv(file,thresh):

    with open(file) as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            result.append(row[thresh - 2:thresh])
        return result

def list2dict(result):
    
    for _ in list(range(20)):
        st_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
        string_result = [result[r] for r in st_list]
        row_st = [int(i) - 1 for i in st_list]
        number_result = [result[r] for r in row_st]
        dic = {key: val for key, val in zip(number_result, string_result)}
        return dic
    #dic_memories = list2dict(row)
    #dic.update(dic_memories)
    #pickle_dump(dic, "dictonary.pickle")
    #print(pickle_load('dictonary.pickle'))

def pickle_dump(obj, path):
    with open(path, mode='wb') as f:
        pickle.dump(obj,f)

def pickle_load(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
        return data

if __name__ == "__main__":
    
    f = "./datas/memories_up.csv"
    thresh_list = [2, 4, 6, 8, 10]
    lis = []
    for th in thresh_list:
        result_1 = setup_csv(f, th)
        row = list(itertools.chain.from_iterable(result_1))
        lis.append(result_1[0:])
    print("---------- Menu ----------")
    print("数字変換表暗記メニュー\n01~20 : type 0\n21~40 : type 1\n41~60 : type 2\n61~80 : type 3\n81~00 : type 4")
    print("--------------------------")

    i = int(input("Please number of type : "))
    category = lis[0:][i]
    incorrect_list = []
    for qes in category:
        ans = qes[1]
        num = qes[0]
        my_ans = input(num + " : ")
        if my_ans == ans:
            print("正解です")
        else:
            print("不正解です")
            incorrect_list.append(qes)
    print("Process finish!")
    print("--------------------------")
    if len(incorrect_list) == 0:
        print("This process is complete")
    else:
        print("Incorrect answer")
        for a in incorrect_list:
            print(a)


