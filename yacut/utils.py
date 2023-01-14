import random
import string

from .models import URLMap


def get_unique_short_id():
    amount = 6
    random_short = "".join(
        random.choices(string.ascii_letters + string.digits, k=amount)
    )
    if URLMap.query.filter_by(short=random_short).first():
        random_short = get_unique_short_id()
    return random_short
