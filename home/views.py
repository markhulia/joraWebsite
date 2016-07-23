from django.shortcuts import render, get_object_or_404
from .models import User, Individual


# Create your views here.
def index(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return render(request, 'home/index.html', context)


def detail(request, user_id):
    # try:
    #     user = User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     raise Http404('User does not exist')

    # instead of try: catch: we can use get_object_or_404
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'home/detail.html', {'user': user})


def married(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        selected_user = user.individual_set.get(pk=request.POST['user'])

    except(KeyError, Individual.DoesNotExist):
        return render(request, 'home/detail.html', {'user':user,
                                                    'error_message':'The person has vanished'})

    else:
        selected_user.is_married=True
        selected_user.save()
        return render(request, 'home/detail.html', {'user': user})









