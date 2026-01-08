from django.shortcuts import render
from django.http import JsonResponse

# import Thought model
from .models import Thought

# thought views 
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def create_thought(request):
    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "error": "Auth required"}, status=403)

    content = request.POST.get("content")
    niche = request.POST.get("niche", None)
    print(request.POST)

    if not content:
        return JsonResponse({"success": False, "error": "Empty thought"})

    thought = Thought.objects.create(
        author=request.user,
        content=content,
        niche=niche
    )
    print(thought)

    return JsonResponse({
        "success": True,
        "thought_id": thought.id
    })



def edit_thought(request, thought_id):
    return render(request, 'thoughts/edit_thought.html', {'thought_id': thought_id})

def delete_thought(request, thought_id):
    return render(request, 'thoughts/delete_thought.html', {'thought_id': thought_id})  

def view_thought(request, thought_id):
    return render(request, 'thoughts/view_thought.html', {'thought_id': thought_id})
