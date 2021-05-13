import random
from textblob import TextBlob
import emotion

# RESPONSES AND QUESTIONS ARE NOT YET FINAL
# FOR TESTING LANG SA WEB APP
# PERO GUMAGANA NA YUNG EMOTION TAGGING

# 1. Name and nickname conversation
print('Hello, what is your name?')
name = input()
print('Do you have a nickname?')
ans = input()
if 'y' in ans.lower():
    nickname = input('what is your nickname: ')
    print('Good to meet you ' + nickname)

# 2. Greeting selection
nickname = ans
greetings = [
    'How are you today ' + nickname + '?',
    'Hello ' + nickname + ' how are you feeling?',
    'Greetings ' + nickname + ', are you well?',
    'How are things going ' + nickname + '?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
    print('Glad you are doing well')
else:
    print('Sorry to hear that')

# 3. Several random opinions on topic
topics = [
    'Social Media',
    'COVID-19',
    'online classes',
    'having friends',
    'hobbies',
]

questions = [
    'What is your take on ',
    'What do you think about ',
    'How do you feel about ',
    'What do you reckon about ',
    'I would like your opinion on '
]

input_words = []
for i in range(0, random.randint(4, 5)):
    question = random.choice(questions)
    questions.remove(question)
    topic = random.choice(topics)
    topics.remove(topic)
    print(question + topic + '?')
    answer = input().split(" ")
    input_words.extend(answer)

# blob = TextBlob(answer)

# input_words = []
# n = answer.split(" ")
# input_words.append(n)

# if blob.polarity > 0.5:
# print('Wow, you really love ' + topic)
# elif blob.polarity > 0.1:
# print('Well, you clearly like ' + topic)
# elif blob.polarity < -0.5:
# print('Oh, you totally hate ' + topic)
# elif blob.polarity < -0.5:
# print("So you don't like " + topic)
# else:
# print('That is a very neutral view on ' + topic)

#    if blob.subjectivity > 0.6:
#       print('and you are so biased')
#    elif blob.subjectivity > 0.3:
#     print('and you are a bit biased')
#   else:
#     print('and you are quite objective')

# 4. Random goodbye
result = ' Here are your results'
goodbyes = [
    'Good talking to you, ' + nickname + result,
    'Thank you.' + result,
    'Okay, bye bye' + result,
    'Have a good day!' + result,
    'Catch you later, ' + nickname
]

print(random.choice(goodbyes))
print(input_words)

emotion.emotion_tag(input_words)
