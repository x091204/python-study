from user import *
from post import Post

print("======WELCOME=======")
user_one.get_user_infor()
print("========================")
user_one.change_job_titile("Devops engineer")
user_one.get_user_infor()
print("========================")
user_one.change_passwrod("nomoreasecret")
user_one.get_user_infor()
print("========================")
new_post = Post("learning python........",user_one.name)
new_post.get_post_info()
