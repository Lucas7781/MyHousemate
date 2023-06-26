from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import User, House, Task

def showUsers(request):
    users = User.objects.all()
    user_data = []
    for user in users:
        user_data.append({
            'id': user.id,
            'name': user.name,
        })

    return JsonResponse({'users': user_data})

def add_user_template(request):
    # Hardcode user values
    name = 'John Doe'

    # Create a new user
    user = User.objects.create(name=name)
    return JsonResponse({'message': 'User created successfully.'})

def add_house(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    if not is_user_authorized():
        return JsonResponse({'error': 'User not Authorized.'}, status=401)
    
    #Create the house object
    house_name = request.POST.get('house_name')
    house_size = request.POST.get('house_size')
    house = House.objects.create(house_name=house_name, house_size=house_size)
    
    #Get user entry from the database
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)
    
    # Add the creator of the house as a member
    house.members.add(user)

    #Send a successful response
    return JsonResponse({'message': 'House created successfully.'})
    
def add_member_to_house(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    if not is_user_authorized():
        return JsonResponse({'error': 'User not Authorized.'}, status=401)
    
    #Add user to the house
    house_id = request.POST.get('house_name')
    house = House.objects.get(id=house_id)

    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)
    
    #TODO: Ensure that the person is part of the house he is sending an invite from

    house.members.add(user)

    #Send a successful response
    return JsonResponse({'message': 'Memeber added to the house Successfully.'})
    
def add_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    if not is_user_authorized():
        return JsonResponse({'error': 'User not Authorized.'}, status=401)
    
    house_id = request.POST.get('house_name')
    house = House.objects.get(id=house_id)
    
    task_name = request.POST.get('task_name')
    task_description = request.POST.get('task_description')

    #TODO: Make sure that the user belongs to the house they want to add the task
    # Add the task to the database
    task = Task.objects.create(task_name = task_name, house = house, task_description = task_description)
    
    #Send a successful response
    return JsonResponse({'message': 'Task created successfully.'})

#TODO: Implement function
def is_user_authorized():
    return True