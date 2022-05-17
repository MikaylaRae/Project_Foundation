from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
class Comment:
    db_name = 'tech_space'
    
    def __init__(self,db_data):
        self.id = db_data['id']
        self.content = db_data['content']
        self.author = db_data['author']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.post_id = db_data['post_id']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comments;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_comments = []
        for row in results:
            print(row['content'])
            all_comments.append( cls(row) )
        return all_comments
    
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM comments WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )
    
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO comments (content, user_id, post_id) VALUES (%(content)s, %(user_id)s, %(post_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def post_with_comment(cls,data):
        query = "SELECT * FROM posts as posts JOIN comments as comments on comments.post_id = posts.id JOIN users on comments.user_id = users.id WHERE comments.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_comments_for_one_post(cls,data): 
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id WHERE post_id = %(post_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        comments = []
        for row in results: 
            one_comment = (cls(row))
            one_comment.user = user.User.get_by_id({"id": row["users.id"]})
            comments.append(one_comment)
        return comments 

# @staticmethod
#     def validate_comment(user):
#         is_valid = True
#         query = "SELECT * FROM users WHERE email = %(email)s;"
#         results = connectToMySQL(User.db_name).query_db(query,user)
#         if len(results) >= 1:
#             flash("Email already taken.","register")
#             is_valid=False
#         if not EMAIL_REGEX.match(user['email']):
#             flash("Invalid Email!!!","register")
#             is_valid=False
#         if len(user['first_name']) < 3:
#             flash("First name must be at least 3 characters","register")
#             is_valid= False
#         if len(user['last_name']) < 3:
#             flash("Last name must be at least 3 characters","register")
#             is_valid= False
#         if len(user['username']) < 3:
#             flash("Username must be at least 3 characters","register")
#             is_valid= False
#         if len(user['password']) < 5:
#             flash("Password must be at least 5 characters","register")
#             is_valid= False
#         if user['password'] != user['confirm']:
#             flash("Passwords don't match","register")
#         return is_valid
    