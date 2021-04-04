target_profile ="thebetterindia"

from instaloader import Instaloader, Profile
loader = Instaloader()

profile = Profile.from_username(loader.context, target_profile)

num_followers = profile.followers

x=profile.full_name
print(target_profile)
print(profile.full_name)
print(profile.biography)
print(profile.followees)
print(num_followers)
print(profile.get_profile_pic_url())
print(profile.business_category_name)
print(profile.mediacount)
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