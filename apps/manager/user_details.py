import datetime
from .models import UserProfile
 # User details pipeline
def user_details(strategy, details, response, user=None, *args, **kwargs):
    if user: # ...
            # Just created the user?
        if kwargs['is_new']:
            attrs = {'user': user}
            # I am using also Twitter backend, so I am checking if It's FB
            # or Twitter. Might be a better way of doing this
            if strategy.backend.__class__.__name__ == 'FacebookOAuth2':
            # We should check values before this, but for the example
            # is fine
                fb_data = {
                    'city': response['location']['name'],
                    'gender': response['gender'],
                    'locale': response['locale'],
                    'dob': datetime.fromtimestamp(mktime(strptime(response['birthday'], '%m/%d/%Y')))
                }
                attrs = dict(attrs.items() + fb_data.items())
                UserProfile.objects.create(**attrs)
