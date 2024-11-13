def get_user_profile(user_id):
    # existing code

def send_welcome_email(user_id):
    New feature to send an email to a new user
    user = get_user_profile(user_id)
    email.send(user.email, "Welcome to the platform!")
