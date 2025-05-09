import time


def make_bold(function) :
        def function_wrapper():
            return "<b>" + function() + "</b>"
        return function_wrapper

def make_emphesis(function) :
        def function_wrapper():
            return "<em>" + function() + "</em>"
        return function_wrapper

def make_underlines(function) :
        def function_wrapper():
            return "<u>" + function() + "</u>"
        return function_wrapper



class User :
    def __init__(self,name):
        self.name=name
        self.is_logged_in=False


def is_authenticated_decorator(function):
    def function_wrapper(*args):
        if args[0].is_logged_in :
            function(args[0])
    return function_wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"user {user.name} created a blog post")


karim = User("Karim")
karim.is_logged_in = True
create_blog_post(karim)




