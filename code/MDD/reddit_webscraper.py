import praw

import string, re
import pandas as pd

reddit = praw.Reddit(user_agent = True, client_id = "RMEOVED", client_secret = "REMOVED", username = "REMOVED", password = 'REMOVED')

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)

subreddit = reddit.subreddit("redditdev")

print(subreddit.display_name)
# Output: redditdev
print(subreddit.title)
# Output: reddit development
print(subreddit.description)
# Output: a subreddit for dis

url = "https://www.reddit.com/r/AmItheAsshole/comments/1b5z41a/aita_for_telling_my_wife_that_she_would_be/"

post = reddit.submission(url = url)

print(post)

post.title

post.selftext

all_comments = []
for comment in post.comments:
    print(comment.body)
    all_comments.append(comment.body)

all_comments

nta_count = all_comments.count("NTA")

import datetime

subreddit = reddit.subreddit("AmItheAsshole")

posts = subreddit.top(time_filter = "all", limit = None)

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts2 = pd.DataFrame(posts_dict)
top_posts2

posts_dict

all_comments

subreddit2 = reddit.subreddit("AmItheButtface")

posts2 = subreddit2.top(time_filter = "all", limit = None)

start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts2:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts3 = pd.DataFrame(posts_dict)
top_posts3

subreddit3 = reddit.subreddit("amiwrong")

posts3 = subreddit3.top(time_filter = "all", limit = None)

start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts3:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts4 = pd.DataFrame(posts_dict)
top_posts4

subreddit4 = reddit.subreddit("AITAH")
posts4 = subreddit4.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts4:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts

subreddit5 = reddit.subreddit("AmITheAngel")
posts5 = subreddit5.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts5:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts5 = pd.DataFrame(posts_dict)
top_posts5

subreddit6 = reddit.subreddit("EntitledPeople")
posts6 = subreddit6.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '31-12-23 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts6:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts6 = pd.DataFrame(posts_dict)
top_posts6

subreddit7 = reddit.subreddit("AmIOverreacting")
posts7 = subreddit7.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts7:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts7 = pd.DataFrame(posts_dict)
top_posts7

posts_dict

top_posts7

subreddit8 = reddit.subreddit("entitledparents")
posts8 = subreddit8.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts8:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        #for comment in post.comments:
         #   all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts8 = pd.DataFrame(posts_dict)
top_posts8

subreddit9 = reddit.subreddit("pettyrevenge")
posts9 = subreddit9.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts9:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts9 = pd.DataFrame(posts_dict)
top_posts9

subreddit10 = reddit.subreddit("weddingshaming")
posts10 = subreddit10.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts10:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts10 = pd.DataFrame(posts_dict)
top_posts10

subreddit11 = reddit.subreddit("amithedevil")
posts11 = subreddit11.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts11:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts11 = pd.DataFrame(posts_dict)
top_posts11

subreddit12 = reddit.subreddit("TalesFromRetail")
posts12 = subreddit12.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts12:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts12 = pd.DataFrame(posts_dict)
top_posts12

subreddit13 = reddit.subreddit("TalesFromTechSupport")
posts13 = subreddit13.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts13:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts13 = pd.DataFrame(posts_dict)
top_posts13

subreddit14 = reddit.subreddit("justnomil")
posts14 = subreddit14.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts14:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts14 = pd.DataFrame(posts_dict)
top_posts14

subreddit15 = reddit.subreddit("TalesFromTheFrontDesk")
posts15 = subreddit15.top(time_filter = "all", limit = None)
start_date = '01-01-20 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

end_date = '30-4-24 12:00:00'
end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

#all_comments = []
for post in posts15:
    # Date of each posts' creation
    date = post.created
    if start_date < date < end_date:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)
        
        # All comments under the post
        # for comment in post.comments:
        # all_comments.append(comment.body)
 
# Saving the data in a pandas dataframe
top_posts15 = pd.DataFrame(posts_dict)
top_posts15

top_posts15.to_csv('C:/Users/User/Desktop/Reddit webscraped data 10k.csv')

def scrape(subreddit_name):   
    subredditx = reddit.subreddit(subreddit_name)
    postsx = subredditx.top(time_filter = "all", limit = None)
    start_date = '01-01-20 00:00:00'
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

    end_date = '30-4-24 12:00:00'
    end_date = datetime.datetime.strptime(end_date, '%d-%m-%y %H:%M:%S').timestamp()

    #all_comments = []
    for post in postsx:
        # Date of each posts' creation
        date = post.created
        if start_date < date < end_date:
            # Title of each post
            posts_dict["Title"].append(post.title)

            # Text inside a post
            posts_dict["Post Text"].append(post.selftext)

            # Unique ID of each post
            posts_dict["ID"].append(post.id)

            # The score of a post
            posts_dict["Score"].append(post.score)

            # Total number of comments inside the post
            posts_dict["Total Comments"].append(post.num_comments)

            # URL of each post
            posts_dict["Post URL"].append(post.url)

            # All comments under the post
            # for comment in post.comments:
            # all_comments.append(comment.body)

    # Saving the data in a pandas dataframe
    top_postsx = pd.DataFrame(posts_dict)
    return top_postsx

#am i the ahole
#am i the ass
#am i the bad guy
#am i the karen
#am i the idiot
#am i actually the asshole
#am i the jerk
#AITAFiltered

new_top_postsx = scrape("AmITheAhole")
new_top_postsx

new_top_postsx = scrape("AmItheAss")
new_top_postsx

new_top_postsx = scrape("AmITheBadGuy")
new_top_postsx

new_top_postsx = scrape("AmITheKaren")
new_top_postsx

new_top_postsx = scrape("AmItheIdiot")
new_top_postsx

new_top_postsx = scrape("AmIActuallyTheAsshole")
new_top_postsx

new_top_postsx = scrape("AmITheJerk")
new_top_postsx

new_top_postsx = scrape("AITAFiltered")
new_top_postsx

new_top_postsx.to_csv('C:/Users/User/Desktop/Reddit webscraped data 14k.csv')

