class User:
    def __init__(self, email, name,password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_passwrod(self, new_passwrod):
        self.password = new_passwrod

    def change_job_titile(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_infor(self):
        print(f"Email: {self.email}")
        print(f"Name: {self.name}")
        print(f"Password: {self.password}")
        print(f"Current Job Title: {self.current_job_title}")


user_one = User("anbe@gmail.com","anbe","itisasecret","devops student")

