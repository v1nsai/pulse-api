import json
from django.http import JsonResponse
from django.shortcuts import render

from pulse_api.post.models import Post

def get_posts_by_user(request, user_id):
    """
    Retrieve all posts created by a specific user.

    Args:
        request: The HTTP request object.
        user_id: The ID of the user whose posts are to be retrieved.

    Returns:
        JsonResponse: A JSON response containing a list of posts.
    """
    posts = Post.objects.filter(author_id=user_id).values()
    return JsonResponse(list(posts), safe=False)

def get_posts_by_tag(request, tag_name):
    """
    Retrieve all posts associated with a specific tag.

    Args:
        request: The HTTP request object.
        tag_name: The name of the tag whose posts are to be retrieved.

    Returns:
        JsonResponse: A JSON response containing a list of posts.
    """
    posts = Post.objects.filter(tags__name=tag_name).values()
    return JsonResponse(list(posts), safe=False)

def get_post_by_id(request, post_id):
    """
    Retrieve a post by its ID.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post to retrieve.

    Returns:
        JsonResponse: A JSON response containing the post details.
    """
    post = Post.objects.filter(id=post_id).values()
    return JsonResponse(list(post), safe=False)

def create_post(request):
    """
    Create a new post.

    Args:
        request: The HTTP request object containing the post data in the body.

    Returns:
        JsonResponse: A JSON response with the ID of the created post and a success message.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post.objects.create(**data)
        return JsonResponse({"id": post.id, "message": "Post created successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def update_post(request, post_id):
    """
    Update an existing post.

    Args:
        request: The HTTP request object containing the updated post data in the body.
        post_id: The ID of the post to update.

    Returns:
        JsonResponse: A success message if the update is successful.
        JsonResponse: An error message if the request method is invalid or an error occurs.
    """
    if request.method == "PUT":
        data = json.loads(request.body)
        Post.objects.filter(id=post_id).update(**data)
        return JsonResponse({"message": "Post updated successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def delete_post(request, post_id):
    """
    Delete a post by its ID.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post to delete.

    Returns:
        JsonResponse: A success message if the deletion is successful.
        JsonResponse: An error message if the request method is invalid or an error occurs.
    """
    if request.method == "DELETE":
        Post.objects.filter(id=post_id).delete()
        return JsonResponse({"message": "Post deleted successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)
