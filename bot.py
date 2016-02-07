import praw


reddit_id = "dshelper_bot"
reddit_pw = ""

agent_name = ("Oak's Machine 1.0")

r = praw.Reddit(user_agent = agent_name)
r.login(reddit_id, reddit_pw, disable_warning = True) #API based login is apparently going to be disabled in future praw updates
													  #To display that warning change the parameter to False or delete argument

subreddit = r.get_subreddit("darksouls")

for submission in subreddit.get_hot(limit = 5):
	print submission.title