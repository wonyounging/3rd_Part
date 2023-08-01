from chatbot.Preprocess1 import Preprocess1

sent = "내일 오전 10시에 짜장면 주문하고 싶어"

p = Preprocess1(userdic='c:/workspace3/FoodShop/data/user_dic.tsv')
#      클래스 = > 메모리, 객체

pos = p.pos(sent)

keywords = p.get_keywords(pos, without_tag=False)

print(keywords)