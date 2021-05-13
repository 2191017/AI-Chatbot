from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer


def emotion_tag(text):

    final_words = []
    for word in text:
        if word not in stopwords.words('english'):
            final_words.append(word)
            print(final_words)

    lemma_words = []
    for word in final_words:
        word = WordNetLemmatizer().lemmatize(word)
        lemma_words.append(word)
        print(lemma_words)

    emotion_list = []
    with open('C:/Users/lois/Desktop/emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in lemma_words:
                emotion_list.append(emotion)
                print(emotion_list)
                w = Counter(emotion_list)
                print(w)

    fig, ax1 = plt.subplots()
    fig.set_size_inches(20, 8)
    plt.rcParams.update({'font.size': 100})
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.xticks(rotation=90)
    plt.savefig('graph.png')
    plt.show()

#replace with method from trained and tested data
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

# sentiment_analyse(cleaned_text)
