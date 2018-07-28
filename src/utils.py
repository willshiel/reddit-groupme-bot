from models import Submission

def convert_to_submission(reddit_sub):
    return Submission(reddit_sub.id,
                   reddit_sub.title,
                   reddit_sub.ups,
                   reddit_sub.downs,
                   reddit_sub.author.name
        )