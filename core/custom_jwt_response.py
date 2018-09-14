from datetime import timedelta, datetime
from project import settings


def jwt_response_payload_handler(token, user=None, request=None):

	return {
		'token': token,
		'expiration_date': datetime.today() + settings.JWT_EXPIRATION_DELTA
	}