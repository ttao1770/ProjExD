from random import choices, randint 
import datetime
from secrets import choice
if __name__ == "__main__":

    #問題をキー，正解リストを値とした辞書
    qa_dict = {"サザエの旦那の名前は？" : ["マスオ","ますお"],"カツオの妹の名前は？":["ワカメ","わかめ"],"タラオはカツオから見てどんな関係？":["甥","おい","甥っ子","おいっこ"]}

    ans = choice(list(qa_dict.items())) #listの番号

    print("問題",ans[0])#問題を表示

    st = datetime.datetime.now()

    item = input("答えを入力してください＞　")
    ed = datetime.datetime.now()
    if item in ans[1] :
        
        print("(・∀・)ｲｲﾈ!!  正解")
        
    else :
        print("不正解")

    print(f"所要時間は{(ed-st).seconds}秒です。")
    