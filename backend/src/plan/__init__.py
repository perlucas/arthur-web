class UserPlan:

    def __init__(self, max_allowed_active_searches: int, max_allowed_searches: int):
        self._max_allowed_active_searches = max_allowed_active_searches
        self._max_allowed_searches = max_allowed_searches

    def can_add_active_search(self, current_active_searches: int) -> bool:
        return current_active_searches < self._max_allowed_active_searches
    
    def can_add_any_search(self, current_searches: int) -> bool:
        return current_searches < self._max_allowed_searches
    

plans = {
    "demo": UserPlan(1, 3),
    "premium": UserPlan(3, 10),
}