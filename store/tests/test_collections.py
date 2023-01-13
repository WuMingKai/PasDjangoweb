from rest_framework import status
import pytest

@pytest.fixture
def create_collection(api_client): # This is the tricky part that if has collection as parameter here, and
  def do_create_collection(collection): # replace the following object(, collection) there, pytest will think this is a fixture, then there is not this fixture by this name, you will get an error.
    return api_client.post('/store/collections/', collection) # So we wrap this line inside an inner function.
  return do_create_collection # return the inner function.

@pytest.mark.django_db
class TestCreateCollection:
  def test_if_user_is_anonymous_returns_401(self, create_collection):
    response = create_collection({'title':'a'}) # closure.
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

  def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
    authenticate() # closure
    
    response = create_collection({'title':'a'}) # closure.

    assert response.status_code == status.HTTP_403_FORBIDDEN

  def test_if_data_is_invalid_returns_400(self, authenticate, create_collection):
    authenticate(is_staff=True) # closure

    response = create_collection({'title':''}) # closure.

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['title'] is not None
    
  def test_if_data_is_valid_returns_201(self, authenticate, create_collection):
    authenticate(is_staff=True) # closure

    response = create_collection({'title':'a'}) # closure.

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['id'] > 0
    
"""
format the tests:
  def XXXX
    Arrange part
    <blank>
    Action part
    <blank>
    Assert part
"""