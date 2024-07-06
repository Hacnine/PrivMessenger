from rest_framework.throttling import UserRateThrottle


class AbdullahRateThrottle(UserRateThrottle):
    scope = 'abdullah'