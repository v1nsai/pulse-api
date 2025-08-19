import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from pulse_api.user.models import CustomUser as User

class UserView(LoginRequiredMixin, View):
    def get_user_by_id(self, request, user_id):
        """
        Retrieve a user by their ID.

        Args:
            request: The HTTP request object.
            user_id: The ID of the user to retrieve.

        Returns:
            JsonResponse: A JSON response containing the user details.
        """
        user = User.objects.filter(id=user_id).values()
        return JsonResponse(list(user), safe=False)

    def create_user(request):
        """
        Create a new user.

        Args:
            request: The HTTP request object containing the user data in the body.

        Returns:
            JsonResponse: A JSON response with the ID of the created user and a success message.
        """
        if request.method == "POST":
            data = json.loads(request.body)
            user = User.objects.create(**data)
            return JsonResponse({"id": user.id, "message": "User created successfully."})
        return JsonResponse({"error": "Invalid request method."}, status=400)

    def update_user(request, user_id):
        """
        Update an existing user.

        Args:
            request: The HTTP request object containing the updated user data in the body.
            user_id: The ID of the user to update.

        Returns:
            JsonResponse: A success message if the update is successful.
            JsonResponse: An error message if the request method is invalid or an error occurs.
        """
        if request.method == "PUT":
            data = json.loads(request.body)
            User.objects.filter(id=user_id).update(**data)
            return JsonResponse({"message": "User updated successfully."})
        return JsonResponse({"error": "Invalid request method."}, status=400)

    def delete_user(request, user_id):
        """
        Delete a user by their ID.

        Args:
            request: The HTTP request object.
            user_id: The ID of the user to delete.

        Returns:
            JsonResponse: A success message if the deletion is successful.
            JsonResponse: An error message if the request method is invalid or an error occurs.
        """
        if request.method == "DELETE":
            User.objects.filter(id=user_id).delete()
            return JsonResponse({"message": "User deleted successfully."})
        return JsonResponse({"error": "Invalid request method."}, status=400)
