import pytest
from unittest.mock import patch
from main import EnviaEmail, ClientError

@pytest.fixture
def send_email_instance():
    send_email = EnviaEmail()
    send_email.registered_sender = 'jmanzo@michel.com.mx'
    send_email.issued_to = 'jose.prieto@michel.com.mx'
    send_email.moded_subject = 'Prueba de envío de correo para'
    return send_email

@patch('main.boto3.client')
def test_send_email(mock_boto3_client, send_email_instance):
    # Mocking the boto3.client method to avoid actual AWS calls during testing

    # Mocking the send_raw_email method to simulate a successful response
    mock_ses = mock_boto3_client.return_value
    mock_ses.send_raw_email.return_value = {'MessageId': 'dummy_message_id'}

    # Call the method under test
    send_email_instance.send_email()

    # Assert that the send_raw_email method was called with the expected arguments
    mock_ses.send_raw_email.assert_called_once_with(
        Source=send_email_instance.registered_sender,
        Destinations=[send_email_instance.issued_to],
        RawMessage={'Data': str}
    )

@patch('main.boto3.client')
def test_send_email_failure(mock_boto3_client, send_email_instance):
    # Mocking the boto3.client method to avoid actual AWS calls during testing

    # Mocking the send_raw_email method to simulate a ClientError
    mock_ses = mock_boto3_client.return_value
    mock_ses.send_raw_email.side_effect = ClientError({}, 'SendRawEmail')

    # Call the method under test
    send_email_instance.send_email()

    # Assert that the send_raw_email method was called with the expected arguments
    mock_ses.send_raw_email.assert_called_once_with(
        Source=send_email_instance.registered_sender,
        Destinations=[send_email_instance.issued_to],
        RawMessage={'Data': str}
    )
