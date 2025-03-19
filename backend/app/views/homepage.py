from django.http import JsonResponse

def prueba_view(request):
    if request.method == "GET":
        print()
        print()
        print()
        print()
        print("KAKAKKAKAK")
        print()
        print()
        print()
        print()
        response = JsonResponse({"mensaje": "Hola desde Django"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
