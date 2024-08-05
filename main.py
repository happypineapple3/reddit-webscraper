import praw
import keys

reddit = praw.Reddit(
    client_id=keys.CLIENT_ID,
    client_secret=keys.CLIENT_SECRET,
    user_agent=keys.USER_AGENT
)

def get_top_posts(subreddit_name, top_n=3):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = []

    for submission in subreddit.top(limit=top_n):
        top_posts.append({
            'title': submission.title,
            'score': submission.score,
            'url': submission.url
        })

    return top_posts

def main():
    subreddit_name = 'AmItheAsshole'  # Replace with the target subreddit
    top_posts = get_top_posts(subreddit_name)

    print("Top Posts:")
    for post in top_posts:
        print(f"Title: {post['title']}, Score: {post['score']}, URL: {post['url']}")

if __name__ == "__main__":
    main()