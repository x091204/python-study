class Post:
    def __init__(self, post, author):
        self.post = post
        self.author = author

    def get_post_info(self):
        print(f"post: {self.post} written by {self.author}")
