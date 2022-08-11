class User:

    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Jack", "001")
user2 = User("angela", "002")
user1.follow(user2)
print(user1.followers, user1.following)
