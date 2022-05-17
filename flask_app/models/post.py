from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, comment


class Post:
    db_name = 'tech_space'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.content = db_data['content']
        self.author = db_data['author']
        self.created_at = db_data['created_at']
        self.updated_at = db_data ['updated_at']
        self.user = user.User.get_by_id({"id": db_data['user_id']})
        # self.comments = []
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts (content, author, user_id) VALUES (%(content)s, %(author)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        print(results)
        all_posts = []
        for row in results:
            one_post = cls(row)
            print(comment.Comment.get_comments_for_one_post({"post_id": row ["id"]}))
            one_post.comments = comment.Comment.get_comments_for_one_post({"post_id": row ["id"]})
            all_posts.append( one_post )
        return all_posts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET content=%(content)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def post_with_username(cls,data):
        query = "SELECT users.username, posts.content FROM users LEFT JOIN posts ON users.id = posts.user_id;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    
    @classmethod
    def get_post_with_comment(cls, data):
        query = "SELECT * FROM posts LEFT JOIN comments ON comments.post_id = posts.id LEFT JOIN users ON comments.user_id = users.id WHERE posts.id = %(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        # results will be a list of posts with the attached comments
        post = cls(results[0])
        for row_from_db in results: 
        #Now we parse the user data to make instances of comments and add them into our list. 
            comment_data = {
                "id": row_from_db["users.id"], 
                "first_name": row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "username": row_from_db["username"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["comments.created_at"],
                "updated_at" : row_from_db ["comments.updated_at"]
            }
            post.comments.append(comment.Comment(comment_data))
        return post 


    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['content']) < 3:
            is_valid = False
            flash("Your post must be at least 3 characters","post")
        return is_valid
    
