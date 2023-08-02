from chatbot.Preprocess2 import Preprocess2
from chatbot.NerModel import NerModel

p = Preprocess2(word2index_dic='c:/workspace3/FoodShop/data/chatbot_dict.bin',
               userdic='c:/workspace3/FoodShop/data/user_dic.tsv')

ner = NerModel(model_name='c:/workspace3/FoodShop/model/ner_model.h5', proprocess=p)

query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)

print(predicts)
print(tags)