from models.submission import Submission

def convert_to_submission(reddit_sub):
    return Submission(reddit_sub.id,
                   reddit_sub.title,
                   reddit_sub.ups,
                   reddit_sub.downs,
                   reddit_sub.author.name,
                   reddit_sub.url
        )

def contains_url(reddit_sub):
    return reddit_sub['url'] is not None and reddit_sub['url'] != ''