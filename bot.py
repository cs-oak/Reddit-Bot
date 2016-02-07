import praw
import pdb
import os
import re

reddit_id = "dshelper_bot"
reddit_pw = ""

agent_name = ("Dark Souls Helper 1.0")

# API based login is apparently going to be disabled in future praw updates
# To display that warning change the parameter to False or delete argument

r = praw.Reddit(user_agent = agent_name)
r.login(reddit_id, reddit_pw, disable_warning = True)

# Initialize subreddit (will be on a temporary subreddit until successful deployment)
subreddit = r.get_subreddit("pythonforengineers")

# Make/Check file for replied-to posts 
if not os.path.isfile("replied_posts.txt"):
	replied_to = []
else:
	with open("replied_posts.txt", "r") as postfile:
		replied_to = postfile.read()
		replied_to = replied_to.split("\n")
		replied_to = filter(None, replied_to)

# Check for target strings and reply to posts
# Check for duplicates and avoid spamming


for submission in subreddit.get_hot(limit = 3):
	if submission.id not in replied_to:
		for comment in submission.comments:
			if re.search("i can't see the sign", comment.body, re.IGNORECASE):
				comment.reply("You need humanity to see the sign!")
		if re.search("Help with O&S", submission.title, re.IGNORECASE):
			submission.add_comment("Try Solaire's white sign on the left staircase where the archer is! Remember to be in human form and stock up on humanity for future attempts!")
			replied_to.append(submission.id)

# Append to replied-posts
with open("replied_posts.txt", "w") as postfile:
	for pid in replied_to:
		postfile.write(pid + "\n")