from src.common.use_case import UseCaseResult

class JsonPresenter:
    
    def present(self, result: UseCaseResult) -> dict | list[dict]:
        if result.is_error():
            return self._present_error(result)
        return self._present_success(result)
    

    def _present_error(self, result: UseCaseResult) -> dict:
        # TODO: implement concrete error handling
        return {}
    
    def _present_success(self, result: UseCaseResult) -> dict | list[dict]:
        # Note: override this method
        return {}