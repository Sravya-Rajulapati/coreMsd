import random
import string

import boto3
from rest_framework import serializers

from .models import UserAccount


class UserRegistrationSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)

    class Meta:
        model = UserAccount

    def create(self, validated_data):
        """
        Create a new user account using the provided mobile number.
        You can add logic here to generate and send an OTP to the user's mobile number.
        """
        mobile_number = validated_data.get('mobile_number')

        def generate_otp(length=6):
            """Generate a random OTP of the specified length."""
            characters = string.digits
            otp = ''.join(random.choice(characters) for _ in range(length))
            return otp

        def send_sms_otp(mobile_number, otp):
            client = boto3.client('ses', region_name='your_aws_region')
            response = client.send_templated_email(
                Source='your_ses_verified_email',
                Destination={'ToAddresses': [mobile_number]},
                Template='your_ses_template_name',
                TemplateData=f"{{'otp': '{otp}'}}",
            )

            return response

        # After OTP generation and sending, you can proceed to create the user account.

        # Here, we'll assume that the user account is created without OTP verification.

        user = UserAccount(mobile_number=mobile_number)
        user.save()
        return user
