import csv
import itertools

def setup_csv(file,thresh):

    with open(file) as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            #print(row[:2])
            result.append(row[thresh - 2:thresh])
            #result.append(row)
        return result

def list2dict(result):

    st_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    string_result = [row[r] for r in st_list]
    row_st = [int(i) - 1 for i in st_list]
    number_result = [row[r] for r in row_st]
    dic = {int(key): val for key, val in zip(number_result, string_result)}
    print(dic)

if __name__ == "__main__":
    
    f = "./datas/memories_up.csv"
    thresh_list = [2, 4, 6, 8, 10]
    for th in thresh_list:
        result_1 = setup_csv(f, th)
        row = list(itertools.chain.from_iterable(result_1))
        dic_memories = list2dict(row)
        st_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        string_result = [row[r] for r in st_list]
        row_st = [int(i) - 1 for i in st_list]
        number_result = [row[r] for r in row_st]
        dic = {int(key): val for key, val in zip(number_result, string_result)}
        print(dic)

# 仕様 : DB作成
# 完成形 : {01:moji, 02:moji, ...} 
 
# 仕様 : 数字に対応する文字列を表示するアプリケーション制作
# 完成形 : 数字欄に文字列を入力すると正解か不正解か表示する

