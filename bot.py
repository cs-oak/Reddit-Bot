import praw

agent_name = ("Oak's Machine 1.0")

r = praw.Reddit(user_agent = agent_name)
subreddit = r.get_subreddit("darksouls")

for submission in subreddit.get_hot(limit = 5):
	print submission.title