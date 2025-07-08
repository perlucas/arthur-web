class PlanExpired(Exception):
    code = 'CURRENT_PLAN_EXPIRED'

class UserLimitsError(Exception):
    code = 'USER_ABOVE_LIMITS'

class PlanLimitsError(Exception):
    code = 'CURRENT_PLAN_LIMITS'