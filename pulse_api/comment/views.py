from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from .models import Comment

class CommentView(LoginRequiredMixin, View):
    @staticmethod
    def get_comments_by_post_id(request, post_id):
        """
        Retrieve all comments for a given post ID.

        Args:
            request: The HTTP request object.
            post_id: The ID of the post for which comments are to be retrieved.

        Returns:
            JsonResponse: A JSON response containing a list of comments.
        """
        comments = Comment.objects.filter(post_id=post_id).values()
        return JsonResponse(list(comments), safe=False)

    @staticmethod
    def get_comments_by_comment_id(request, comment_id):
        """
        Retrieve a comment by its ID.

        Args:
            request: The HTTP request object.
            comment_id: The ID of the comment to retrieve.

        Returns:
            JsonResponse: A JSON response containing the comment details.
        """
        comments = Comment.objects.filter(id=comment_id).values()
        return JsonResponse(list(comments), safe=False)

    @staticmethod
    def create_comment(request):
        """
        Create a new comment.

        Args:
            request: The HTTP request object containing the comment data in the body.

        Returns:
            JsonResponse: A JSON response with the ID of the created comment and a success message.
            HttpResponseBadRequest: If the request method is invalid or an error occurs.
        """
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                comment = Comment.objects.create(**data)
                return JsonResponse({"id": comment.id, "message": "Comment created successfully."})
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {str(e)}")
        return HttpResponseBadRequest("Invalid request method.")

    def update_comment(request, comment_id):
        """
        Update an existing comment.

        Args:
            request: The HTTP request object containing the updated comment data in the body.
            comment_id: The ID of the comment to update.

        Returns:
            JsonResponse: A success message if the update is successful.
            HttpResponseBadRequest: If the request method is invalid or an error occurs.
        """
        if request.method == "PUT":
            try:
                data = json.loads(request.body)
                Comment.objects.filter(id=comment_id).update(**data)
                return JsonResponse({"message": "Comment updated successfully."})
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {str(e)}")
        return HttpResponseBadRequest("Invalid request method.")

    def delete_comment(request, comment_id):
        """
        Delete a comment.

        Args:
            request: The HTTP request object.
            comment_id: The ID of the comment to delete.

        Returns:
            JsonResponse: A success message if the deletion is successful.
            HttpResponseBadRequest: If the request method is invalid or an error occurs.
        """
        if request.method == "DELETE":
            try:
                Comment.objects.filter(id=comment_id).delete()
                return JsonResponse({"message": "Comment deleted successfully."})
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {str(e)}")
        return HttpResponseBadRequest("Invalid request method.")

