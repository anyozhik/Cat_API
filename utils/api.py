from utils.http_methods import HttpMethods
import os

"""Methods for testing cat API"""

base_url = "https://api.thecatapi.com/v1" #base URL

class CatApi:
    """Method for uploading a new cat photo"""
    @staticmethod
    def upload_new_photo():
        post_resource = "/images/upload"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        files = [('file', ('IMG_1.jpeg', open(f'{os.getcwd()}\\tests\\IMG_1.jpeg', 'rb'), 'image/jpeg'))]
        result_post = HttpMethods.post_upload(post_url, files)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking an uploaded photo"""
    @staticmethod
    def get_new_photo(photo_id):

        get_resource = "/images/" #resource for a get request
        get_url = f"{base_url}{get_resource}{photo_id}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for deleting an uploaded photo"""
    @staticmethod
    def delete_new_photo(photo_id):
        delete_resource = "/images/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{photo_id}"
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.status_code)
        return result_delete

    """Method for checking a photo after deleting"""

    @staticmethod
    def get_deleted_photo(photo_id):
        get_resource = "/images/"  # resource for a get request
        get_url = f"{base_url}{get_resource}{photo_id}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.status_code)
        return result_get

    """Method for searching images with parameters"""

    @staticmethod
    def get_specific_images(size, mime_type, response_format, order, page, limit):
        get_resource = "/images/search"  # resource for a get request
        get_url = f"{base_url}{get_resource}?size={size}&mime_types={mime_type}&format={response_format}&order={order}&page={page}&limit={limit}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for adding an image to favourites"""

    @staticmethod
    def add_to_favourites(image_id):
        post_resource = "/favourites"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        json_body_image = {"image_id": image_id,
                            "sub_id": "Anka-user"}

        result_post = HttpMethods.post(post_url, json_body_image)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking favourite pictures"""

    @staticmethod
    def get_my_favourites():
        get_resource = "/favourites"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for deleting a picture from the favourites"""

    @staticmethod
    def delete_favourite(favourite_id):
        delete_resource = "/favourites/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{favourite_id}"
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.status_code)
        return result_delete


    """Method for voting for an image"""

    @staticmethod
    def vote_for_an_image(image_id):
        post_resource = "/votes"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        json_body_vote = {"image_id": image_id,
                            "sub_id": "Anka-user",
                           "value":1}

        result_post = HttpMethods.post(post_url, json_body_vote)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking users's votes"""

    @staticmethod
    def get_my_votes():
        get_resource = "/votes"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for deleting a vote"""

    @staticmethod
    def delete_vote(vote_id):
        delete_resource = "/votes/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{vote_id}"
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.status_code)
        return result_delete



