import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

from pulse_api.tag.models import Tag

def get_tags_by_post_id(request, post_id):
    """
    Retrieve all tags associated with a specific post.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post whose tags are to be retrieved.

    Returns:
        JsonResponse: A JSON response containing a list of tags.
    """
    tags = Tag.objects.filter(posts__id=post_id).values()
    return JsonResponse(list(tags), safe=False)

def get_tag_by_name(request, tag_name):
    """
    Retrieve a tag by its name.

    Args:
        request: The HTTP request object.
        tag_name: The name of the tag to retrieve.

    Returns:
        JsonResponse: A JSON response containing the tag details.
    """
    tag = Tag.objects.filter(name=tag_name).values()
    return JsonResponse(list(tag), safe=False)

def create_tag(request):
    """
    Create a new tag.

    Args:
        request: The HTTP request object containing the tag data in the body.

    Returns:
        JsonResponse: A JSON response with the ID of the created tag and a success message.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        tag = Tag.objects.create(**data)
        return JsonResponse({"id": tag.id, "message": "Tag created successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def update_tag(request, tag_id):
    """
    Update an existing tag.

    Args:
        request: The HTTP request object containing the updated tag data in the body.
        tag_id: The ID of the tag to update.

    Returns:
        JsonResponse: A success message if the update is successful.
        JsonResponse: An error message if the request method is invalid or an error occurs.
    """
    if request.method == "PUT":
        data = json.loads(request.body)
        Tag.objects.filter(id=tag_id).update(**data)
        return JsonResponse({"message": "Tag updated successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def delete_tag(request, tag_id):
    """
    Delete a tag by its ID.

    Args:
        request: The HTTP request object.
        tag_id: The ID of the tag to delete.

    Returns:
        JsonResponse: A success message if the deletion is successful.
        JsonResponse: An error message if the request method is invalid or an error occurs.
    """
    if request.method == "DELETE":
        Tag.objects.filter(id=tag_id).delete()
        return JsonResponse({"message": "Tag deleted successfully."})
    return JsonResponse({"error": "Invalid request method."}, status=400)