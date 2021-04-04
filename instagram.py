target_profile ="thebetterindia"

from instaloader import Instaloader, Profile
loader = Instaloader()

profile = Profile.from_username(loader.context, target_profile)

num_followers = profile.followers
num_following=profile.biography
x=profile.full_name
print(num_following)
print(num_followers)
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

for post in profile.get_posts():
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1
    if(total_num_posts==10):
        break;

engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
print(engagement * 100)