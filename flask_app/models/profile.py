from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Profile:
    db_name = 'tech_space'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.job_title = db_data['job_title']
        self.about_me = db_data['about_me']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

    @classmethod
    def create_profile(cls,data):
        if not cls.validate_user(data):
            return False
        else:
            data = cls.parse_user_data(data)
        query = """l
        INSERT INTO profiles (job_title, about_me)
        VALUES (%(job_title)s, %(about_me)s)
        ;"""
        user_id = MySQLConnection(cls.db).query_db(query, data)
        session['user_id'] = user_id
        return user_id
    
    
    # delete
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM profiles;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        # print('-----------------------------------------------------------------')
        # print(results)
        # print('-----------------------------------------------------------------')
        all_profiles = []
        for row in results:
            print(row['job_title'])
            all_profiles.append( cls(row) )
        return all_profiles
        
            
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM profiles WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print('-----------------------------------------------------------------')
        print(results)
        print('-----------------------------------------------------------------')
        if not results: 
            return False      
        return cls( results[0] )

    @classmethod
    def save(cls,data):
        query = "INSERT INTO profiles (job_title, about_me, user_id) VALUES (%(job_title)s, %(about_me)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        print('************, data=', data)
        query = "UPDATE profiles SET about_me = %(about_me)s, job_title = %(job_title)s WHERE user_id = %(id)s;" 
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM profiles WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_profile(profile):
        is_valid = True
        if len(profile['job_title']) < 3:
            is_valid = False
            flash("Job Title must be at least 3 characters","profile")
        if len(profile['about_me']) < 3:
            is_valid = False
            flash("Tell us about yourself in 3 words or more","profile")
        return is_valid