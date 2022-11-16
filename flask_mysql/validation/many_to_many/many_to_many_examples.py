    self.likers = []
    self.likers_ids = []

likers.id

    @classmethod
    def get_all_posts(cls):
        query = '''
        SELECT * FROM posts 
        JOIN users AS poster ON posts.user = poster.id
        LEFT JOIN likes ON posts.id = likes.postId
        LEFT JOIN users AS likers ON likers.id = likes.userId
        '''
        results = connectToMySQL('python_exam').query_db(query)
        all_posts = []
        for row in results:
            if len(all_posts) == 0 or all_posts[len(all_posts)-1].id != row["id"]:
                one_post = cls(row)
                user_data = {
                    "id": row['poster.id'], 
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "password": row['password'],
                    "created_at": row['poster.created_at'],
                    "updated_at": row['poster.updated_at']
                    }
                user_object = users.User(user_data)
                one_post.poster = user_object
                if row['likers.id'] != None:
                    liker_data = {
                        "id": row['likers.id'], 
                        "first_name": row['likers.first_name'],
                        "last_name": row['likers.last_name'],
                        "email": row['likers.email'],
                        "password": row['likers.password'],
                        "created_at": row['likers.created_at'],
                        "updated_at": row['likers.updated_at']
                        }   
                    liker_object = users.User(liker_data)
                    one_post.likers.append(liker_object)
                    one_post.likers_ids.append(liker_object.id)
                all_posts.append(one_post)
            else:
                liker_data = {
                    "id": row['likers.id'], 
                    "first_name": row['likers.first_name'],
                    "last_name": row['likers.last_name'],
                    "email": row['likers.email'],
                    "password": row['likers.password'],
                    "created_at": row['likers.created_at'],
                    "updated_at": row['likers.updated_at']
                    }
                liker_object = users.User(liker_data)
                print("*******************************************************************")
                all_posts[len(all_posts)-1].likers.append(liker_object)
                all_posts[len(all_posts)-1].likers_ids.append(liker_object.id)
        return all_posts
