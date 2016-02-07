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

# Make/Check file for replied-to comments, including child comments		
if not os.path.isfile("replied_comments.txt"):
	replied_to_comments = []
else:
	with open("replied_comments.txt", "r") as postfile:
		replied_to_comments = postfile.read()
		replied_to_comments = replied_to_comments.split("\n")
		replied_to_comments = filter(None, replied_to_comments)

# Check for target strings and reply to posts and comments
# Check for duplicates (using 2 files) and avoid spamming

for submission in subreddit.get_hot(limit = 3):
	# retrive comment forest, flatten out the forest for parsing
	comment_forest = submission.comments
	comments_flat = praw.helpers.flatten_tree(comment_forest)
		
	# reply to comments, check for duplicates
	for comment in comments_flat:
		if comment.id not in replied_to_comments:
			if re.search("I can't see the sign", comment.body, re.IGNORECASE):
				comment.reply("Make sure you have humanity!")
				replied_to_comments.append(comment.id)
	
	# reply to the main submission, of criteria is met
	if submission.id not in replied_to:
		if re.search("Help with O&S", submission.title, re.IGNORECASE):
			submission.add_comment("Try Solaire's white sign on the left staircase where the archer is! Remember to be in human form and stock up on humanity for future attempts!")
			replied_to.append(submission.id)

# Append to replied-posts
with open("replied_posts.txt", "w") as postfile:
	for pid in replied_to:
		postfile.write(pid + "\n")

# Append to replied-comments
with open("replied_comments.txt", "w") as postfile:
	for pid in replied_to_comments:
		postfile.write(pid + "\n")