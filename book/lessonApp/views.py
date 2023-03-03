from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_task_by_id(response, *args, **kwargs):
    task = Task.objects.get(pk=kwargs['pk'])

    return JsonResponse({'Task': TaskSerializer(task, many=False).data})


@api_view(['GET'])
def get_tasks(request, *args, **kwargs):
    tasks = Task.objects.all()

    return JsonResponse({'Tasks': TaskSerializer(tasks, many=True).data})


@api_view(['POST'])
def create_task(request, *args, **kwargs):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return JsonResponse({'Task': serializer.data}, status=201)


@api_view(['PATCH'])
def update_task(request, *args, **kwargs):
    try:
        task = Task.objects.get(pk=kwargs['pk'])
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'})

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    serializer.is_valid()
    serializer.save()

    return JsonResponse({'Task': serializer.data})


@api_view(['DELETE'])
def delete_task(request, *args, **kwargs):
    try:
        task = Task.objects.get(pk=kwargs['pk'])
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'})

    task.delete()

    return JsonResponse({'message': "Task was deleted"})
