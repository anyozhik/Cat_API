import allure
from utils.api import CatApi
from utils.checking import Checking

"""Test for checking methods for the CatAPI"""
@allure.epic("Test for checking main modules: uploading photos, adding to favourites, voting for pictures")
class TestCatAPI:

    @allure.description("Uploading, updating, deleting a new cat photo")
    def test_upload_new_photo(self):

        print("Method post for uploading a photo")
        post_result = CatApi.upload_new_photo()
        check_post = post_result.json()
        photo_id = check_post.get("id")
        Checking.check_status_code(post_result, 201)
        Checking.check_json_token(post_result, ['id', 'url', 'width', 'height', 'original_filename', 'pending', 'approved'])

        print("Method get after post for the photo")
        get_result = CatApi.get_new_photo(photo_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['id', 'url', 'width', 'height', 'sub_id'])

        print("Method delete for the photo")
        delete_result = CatApi.delete_new_photo(photo_id)
        Checking.check_status_code(delete_result, 204)

        print("Method get after delete")
        get_result = CatApi.get_deleted_photo(photo_id)
        Checking.check_status_code(get_result, 400)

        print("Testing of uploading and deleting a new photo has finished successfully.")

    def test_add_to_favourites(self):

        print("Method get for a search of specific images")
        get_result = CatApi.get_specific_images('med', 'jpg', 'json', 'RANDOM', '0', '2' )
        get_json = get_result.json()
        photo_id_1 = get_json[0].get("id")
        photo_id_2 = get_json[1].get("id")
        Checking.check_status_code(get_result, 200)

        print("Method for adding pictures to favourites")
        post_result_1 = CatApi.add_to_favourites(photo_id_1)
        check_post = post_result_1.json()
        favourite_id_1 = check_post.get("id")
        Checking.check_status_code(post_result_1, 200)
        Checking.check_json_token(post_result_1, ['message','id'])

        post_result_2 = CatApi.add_to_favourites(photo_id_2)
        check_post = post_result_2.json()
        favourite_id_2 = check_post.get("id")
        Checking.check_status_code(post_result_2, 200)
        Checking.check_json_token(post_result_2, ['message', 'id'])

        print("Method get for checking favourites")
        get_result = CatApi.get_my_favourites()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 2)

        print("Method delete for the first favourite picture")
        delete_result = CatApi.delete_favourite(favourite_id_1)
        Checking.check_status_code(delete_result, 200)

        print("Method get for checking favourites after the first delete")
        get_result = CatApi.get_my_favourites()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 1)

        print("Method delete for the second favourite picture")
        delete_result = CatApi.delete_favourite(favourite_id_2)
        Checking.check_status_code(delete_result, 200)

        print("Method get for checking favourites after the second delete")
        get_result = CatApi.get_my_favourites()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 0)

        print("Testing of adding pictures to favourites and removing them has finished successfully.")

    @allure.description("Voting for pictures and then removing votes")
    def test_vote_for_pictures(self):
        print("Method get for a search of specific images")
        get_result = CatApi.get_specific_images('med', 'jpg', 'json', 'RANDOM', '0', '2')
        get_json = get_result.json()
        photo_id_1 = get_json[0].get("id")
        photo_id_2 = get_json[1].get("id")
        Checking.check_status_code(get_result, 200)

        print("Method for voting for the picture")
        post_result_1 = CatApi.vote_for_an_image(photo_id_1)
        check_post = post_result_1.json()
        vote_id_1 = check_post.get("id")
        Checking.check_status_code(post_result_1, 201)
        Checking.check_json_token(post_result_1, ['message', 'id', 'image_id', 'sub_id', 'value'])

        post_result_2 = CatApi.vote_for_an_image(photo_id_2)
        check_post = post_result_2.json()
        vote_id_2 = check_post.get("id")
        Checking.check_status_code(post_result_2, 201)
        Checking.check_json_token(post_result_1, ['message', 'id', 'image_id', 'sub_id', 'value'])

        print("Method get for checking votes")
        get_result = CatApi.get_my_votes()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 2)

        print("Method delete for the first vote")
        delete_result = CatApi.delete_vote(vote_id_1)
        Checking.check_status_code(delete_result, 200)

        print("Method get for checking votes after the first delete")
        get_result = CatApi.get_my_votes()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 1)

        print("Method delete for the second vote")
        delete_result = CatApi.delete_vote(vote_id_2)
        Checking.check_status_code(delete_result, 200)

        print("Method get for checking votes after the second delete")
        get_result = CatApi.get_my_votes()
        Checking.check_status_code(get_result, 200)
        Checking.check_len_of_response(get_result, 0)

        print("Testing of voting for the pictures and removing votes has finished successfully.")

