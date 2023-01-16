from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateProduction:
  def test_if_user_is_anonymos_returns_401(self):
    client = APIClient()

    response = client.post('/store/products/', {'title':'a'})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
  def test_if_user_is_not_admin_return_403(self):
    client = APIClient()
    client.force_authenticate(user={})

    response = client.post('/store/products/',{'title':'a'})

    assert response.status_code == status.HTTP_403_FORBIDDEN

# The client is authenticated, and the current is admin, but the data we post to the server 
# is invalid.
  def test_if_data_is_invalid_return_400(self):
    client = APIClient()
    client.force_authenticate(user=User(is_staff=True))

    response = client.post('/store/products/',{'title':''})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['title'] is not None 
  
  def test_if_data_is_valid_return_201(self):
    client = APIClient()
    client.force_authenticate(user=User(is_staff=True))

    response = client.post('/store/products/',{'title':'a'})

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['id'] > 0