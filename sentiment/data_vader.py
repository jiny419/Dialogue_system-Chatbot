"""
         ^---^
        { *w* }
         $    $
        {_|__|_}====
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyser = SentimentIntensityAnalyzer()
df=pd.read_csv('data_sentiment.csv',encoding='utf-8')
print(df.head())

# vader 결과
vaderresult=[]

# 상품리뷰 점수와 같은 경우
truecount = 0

for i in range(df.id.count()):
    # compound결과가 0.05보다 크면 긍정, -0.05보다 작으면 부정
    if analyser.polarity_scores(df.textcontent[i]).get("compound")>0.05:
        vaderresult.append(1)
    elif analyser.polarity_scores(df.textcontent[i]).get("compound")< -0.05:
        vaderresult.append(0)
    else:
        vaderresult.append(3)

    print(df.textcontent[i], df.reviewrating[i], vaderresult[i])

    #자세히 보고 싶다면..
    #print(df.textcontent[i],analyser.polarity_scores(df.textcontent[i]))

for i in range(df.id.count()):
    if vaderresult[i]==df.reviewrating[i]:
        truecount=truecount+1

#정확도
print("정확도 : ",truecount/(df.id.count()))

