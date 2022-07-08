import praw
import os
import time

def makeDownloadLink(subredditName,id):
    defaultLink = f"https://redditvideodl.com/dl.php?url=https%3A%2F%2Fwww.reddit.com%2Fr%2F{subredditName}%2Fcomments%2F"
    link=defaultLink + id + f"%2F"
    return link

#Replace with your own information
reddit = praw.Reddit(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    username=os.getenv("username"),
    password=os.getenv("password"),
    user_agent="<console:FirstBotTest:0.0.5 (by /u/FirstRedditBotTest)>",
)

reddit.read_only=False

#Loops 500000 times and checks if there are new messages
#If there are new messages it gets the information of the post anf makes the download link
#This took 2 days to understand 
for i in range(500000):
    time.sleep(10)
    mentions = reddit.inbox.mentions()
    for message in mentions:
        if message.new:
            if f"u/{str(reddit.user.me())}" in str(message.body):
                reply=f"Hello {str(message.author)} the link is : " + makeDownloadLink(str(message.subreddit), str(message.submission))
                message.reply(body=reply)
                message.mark_read()

#Test code to understand the API better

""""
# inbox = reddit.inbox.all(limit=1)

# subredditName = "FirstRedditBotTesting"
# subredditName = "memes"
# subreddit = reddit.subreddit(subredditName)

# for message in inbox:
#     if message.body=="u/"+str(reddit.user.me()):
#         print(message.author)
#         message.reply(body="Hi!")
#         message.mark_read()

# for post in subreddit.hot(limit=5):
#     downloadLink = defaultDownloadLink
#     # print(post.id,end="\n***\n")
#     # postLink+=str(post.id)+"/"
#     downloadLink+=str(post.id)+f"%2F"
#     print(downloadLink,end="\n\n")

# for message in inbox:
#     if hasattr(message, "body"):
#         print (message.body)
#     print("***********")

# for comment in subreddit.stream.comments():
#     if hasattr(comment, "body"):
#         commentText = comment.body.lower()
#         if (commentText == "hello there"):
#             comment.reply("General Kenoby")
#     print("**********")
"""
