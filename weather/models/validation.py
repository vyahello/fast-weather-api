"""Module contains weather validations API."""


class ValidationError(Exception):
    def __init__(self, error_message: str, status_code: int) -> None:
        super().__init__(error_message)
        self._status_code = status_code
        self._error_message = error_message

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def error_message(self) -> str:
        return self._error_message
