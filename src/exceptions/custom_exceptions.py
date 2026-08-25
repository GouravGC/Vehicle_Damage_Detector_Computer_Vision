class ApplicationException(Exception):
    """Base exception for application-specific errors."""


class ConfigurationError(ApplicationException):
    """Raised when application configuration is invalid."""


class ModelLoadingError(ApplicationException):
    """Raised when the YOLO model cannot be loaded."""


class ImageValidationError(ApplicationException):
    """Raised when an input image is invalid."""


class InferenceError(ApplicationException):
    """Raised when model inference fails."""