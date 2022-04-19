from random import randint 
import datetime
if __name__ == "__main__":

    #問題と解答を羅列する
    question = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    answer = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]

    num = randint(0,2) #listの番号

    print("問題",question[num])

    st = datetime.datetime.now()

    while True :

        item = input("答えを入力してください")

        if item in answer[num] :
            ed = datetime.datetime.now()
            print("正解")
            break
            
        else :
            print("不正解。もう一度")

    print(f"所要時間は{(ed-st).seconds}秒です。")