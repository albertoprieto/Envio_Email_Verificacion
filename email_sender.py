import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class SendEmail():

    def __init__(self, region_name):
        """
        Initialize the SendEmail instance with the boto3 SES client.

        Parameters:
        - region_name (str): The AWS region name.
        """
        self.ses = boto3.client('ses', region_name=region_name)

    @staticmethod
    def read_from_file(file_path):
        """
        Read the content of a file and return its content as a string.

        Parameters:
        - file_path (str): The path to the file to be read.

        Returns:
        - str: The content of the file.
        """
        with open(file_path, 'r') as file:
            return file.read().strip()

    @staticmethod
    def read_body(file_path):
        """
        Read the content of an email body file and return its content as a string.

        Parameters:
        - file_path (str): The path to the file containing the email body.

        Returns:
        - str: The content of the email body file.
        """
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def read_config(config_file_path):
        """
        Read the configuration from a file and return a configuration dictionary.

        Parameters:
        - config_file_path (str): The path to the configuration file.

        Returns:
        - dict: A dictionary containing the configuration.
        """
        config = {}
        with open(config_file_path, 'r') as file:
            for line in file:
                key, value = map(str.strip, line.split(':', 1))
                config[key] = value
        return config

    def send_email(self, sender, recipient, subject, body):
        """
        Send an email using AWS Simple Email Service (SES).

        Parameters:
        - sender (str): The sender's email address.
        - recipient (str): The recipient's email address.
        - subject (str): The email subject.
        - body (str): The email body in HTML format.
        """
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = recipient
        message.attach(MIMEText(body, 'html'))

        try:
            response = self.ses.send_raw_email(
                Source=sender,
                Destinations=[recipient],
                RawMessage={'Data': message.as_string()}
            )

            logging.info(f"Email sent to {recipient}. Response: {response}")

        except ClientError as e:
            logging.error(f"Error sending email to {recipient}. Error: {e}")
