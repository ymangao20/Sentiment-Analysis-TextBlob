from textblob import TextBlob

Feedback1= " the foods in Silang  was awesome "
Feedback2= " the foods in Silang was very good"
blob1= TextBlob(Feedback1)
blob2= TextBlob(Feedback2)

print(blob1.sentiment)
print(blob2.sentiment)