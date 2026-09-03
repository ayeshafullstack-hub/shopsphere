from rest_framework.views import exception_handler

def custom_exception_handler(exc,context):
    response = exception_handler(exc,context)
    if response is not None and response.status__code == 404:
        response.data = {
            "error" : "Product not found"
        }
    return response