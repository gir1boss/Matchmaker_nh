# Nathaly Hernandez 
# Matchmaker Lite - Part 2

# Constants
INTRODUCTION = '''
<h1 style='background-color:DeepPink;'>
<h1 style="border:2px solid Tomato;'

Matchmaker 2021

Well well well... Hello, fancy seeing you here. I see that you are interested in seeing if whether you and I are compatible. 
I mean it's no surprise who wouldn't want to match with me? It's me... come on we both know that I am your dream girl. 
Anyways take this small 5 question quiz, answer correctly and you might have a shot at me. Answer wrong and your future may be doomed
for you may not have a future with me in it.

The way this works is you rate the statements on a scale from 1-5, 5 meaning you strongly agree and 1 being you strongly disagree.

Goodluck, you're gonna need it.. no seriously I am way out of your league. 
'</h1>

'''

QUESTION = [
    'Rocket league is the game of love',
    'Basketball is fun to play and watch',
    'Green is a nice color',
    'Star Wars movies are great',
    'Red is a nice color'
]

DESIRED_RESPONSE = [
    5, #strongly agree
    1, #strongly disagree
    5, #strongly agree
    1, #strongly disagree
    3, #neutral
]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)


# Ask all questions.

response = []
compatibility = []

for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    response.append(userResponse)
    # Todo: Validate response, and ask question again if necessary.

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)

    # String formatting with parameters and place holders.
    print('QUESTION %d compatibility : %d\n' % (i+1, questionCompatibility))

totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c

totalCompatibility *= 100 / MAX_SCORE
print('Total Compatibility: %d\n\n' % (totalCompatibility))

# Todo:  Determine compatibility ranges. 