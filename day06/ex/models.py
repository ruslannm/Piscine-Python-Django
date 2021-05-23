from django.db import models

class Upvote(models.Model):
    user = models.CharField(max_length=150)


class Downvote(models.Model):
    user = models.CharField(max_length=150)    

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    upvote_users = models.ManyToManyField(Upvote)
    downvote_users = models.ManyToManyField(Downvote)

    def upvote(self, username):
        votes = self.upvote_users.all()
        user_voted = False
        for u in votes:
            if u.user == username:
                user_voted = True
                u.delete()
                break
        if not user_voted:
            new_vote = Upvote(user=username)
            new_vote.save()
            self.upvote_users.add(new_vote)
            votes = self.downvote_users.all()
            for u in votes:
                if u.user == username:
                    u.delete()
                    break
            self.save()

    def downvote(self, username):
        votes = self.downvote_users.all()
        user_voted = False
        for u in votes:
            if u.user == username:
                user_voted = True
                u.delete()
                break
        if not user_voted:
            new_vote = Downvote(user=username)
            new_vote.save()
            self.downvote_users.add(new_vote)
            votes = self.upvote_users.all()
            for u in votes:
                if u.user == username:
                    u.delete()
                    break
            self.save()

    def __str__(self):
        return str(self.date.strftime('%Y-%m-%d %H:%M:%S')) + ' ' + \
            self.content + ' by ' + self.author + \
            ' upvotes : ' + str(len(self.upvote_users.all())) + \
            ' downvotes : ' + str(len(self.downvote_users.all()))
            