from api import PetFriends
from settings import valid_email, valid_password, unvalid_password, unvalid_email
import os

pf = PetFriends()
##
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
#1
def test_get_api_key_for_unvalid_user (email=unvalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
#2
def test_get_api_key_with_unvalid_password (email=valid_email, password=unvalid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
##
def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
#3
def test_get_all_pets_with_unvaalid_key(filter=''):
    auth_key = {'key': 'd89929e4803995ef9e686367e87f98ab1367cbfc9828fa40b7b'}
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
#4
def test_get_all_pets_check_content_type_equals_json(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert type(result) == dict
#5
def test_get_all_pets_with_uncorrect_filter(filter='@#%hgfd#2'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
#6
def test_get_my_pets(filter="my_pets"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len (result ['pets']) > 0
##
def test_add_new_pet_with_valid_data(name='Мурка', animal_type='скотиш', age='5', pet_photo='img/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
#7
def test_add_new_pet_simple (name= "Nana", animal_type="cat", age="3"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result ['name'] ==name
#8
def test_add_new_pet_without_name(name="", animal_type='cat', age="5"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result ['name'] == name
#9
def test_add_new_pet_with_wrong_age (name='Мурка', animal_type='скотиш', age='пять'*10, pet_photo='img/cat.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


#10
def test_add_photo_of_pet (name='Nana', animal_type= 'cat', age='3', pet_photo='img/cat.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")
##
def test_successful_update_self_pet_info(name='Nana', animal_type='cat', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")
##
def test_delet_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "img/cat.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()
