from django.http import JsonResponse

HTTP_ERRORS = {
    400: "Solicitud incorrecta. Por favor, verifica los datos enviados.",
    401: "No autorizado. Por favor, proporciona credenciales válidas.",
    403: "Prohibido. No tienes permiso para acceder a este recurso.",
    404: "No encontrado. El recurso solicitado no existe.",
    405: "Método no permitido. Por favor, verifica el método HTTP utilizado.",
    500: "Error interno del servidor. Por favor, intenta nuevamente más tarde.",
    502: "Bad Gateway. El servidor recibió una respuesta inválida.",
    503: "Servicio no disponible. Por favor, intenta nuevamente más tarde.",
    504: "Gateway Timeout. El servidor no respondió a tiempo.",
}

def handle_http_error(status_code):
    message = HTTP_ERRORS.get(status_code, "Error desconocido.")
    return JsonResponse({"error": message}, status=status_code)