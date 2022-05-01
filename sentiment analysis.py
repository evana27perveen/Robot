from textblob import TextBlob
import rawchat

pos_count = 0
pos_correct = 0

s = input()
analysis = TextBlob(s)
pol =analysis.sentiment.polarity
if pol > 0:
    print("Thank you")
elif pol < 0:
    print("Don't say something like this.")
else:
    response = rawchat.response(s)
    print(response)

# with open("positive.txt","r") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.polarity > 0:
#             pos_correct += 1
#         pos_count +=1
#
#
# neg_count = 0
# neg_correct = 0
#
# with open("negative.txt","r") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.polarity <= 0:
#             neg_correct += 1
#         neg_count +=1
#
# print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
# print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))