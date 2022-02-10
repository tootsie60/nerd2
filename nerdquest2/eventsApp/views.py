from telnetlib import GA
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.

def enter(request):
    return render(request, 'enter.html')


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/index')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/welcome')
    return redirect('index')


def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/welcome')
                print(user.id)
        messages.error(request, "Email or password is incorrect")
    return redirect('/index')


def logout(request):
    request.session.flush()
    return redirect('/')


def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/index')
        user = User.objects.get(id=request.session['user_id']),
    context = {

        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'welcome.html', context)


def new_game(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'create_game.html', context)


def create_game(request):
    if 'user_id'not in request.session:
        return redirect('/')
    if request.method == 'POST':
        errors = Game.objects.create_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/welcome')
        # Create a game
        user = User.objects.get(id=request.session['user_id'])
        new_game = Game.objects.create(
            gameType=request.POST['gameType'],
            date=request.POST['date'],
            startTime=request.POST['startTime'],
            endTime=request.POST['endTime'],
            location=request.POST['location'],
            notes=request.POST['notes'],
            creator=user)
        messages.success(request, "New Game Created!")
        print(new_game.creator.id)
        new_game.participants.add(user)
        return redirect('/games')
    return redirect('/games')


def games(request):

    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_games': Game.objects.all(),

    }

    return render(request, 'all_games.html', context)


def one_game(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    # get the clicked group
    context = {
        'one_game': Game.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'one_game.html', context)


def your_games(request):
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'your_games': Game.objects.all().filter(id=request.session['user_id']),

    }
    return render(request, 'your_games.html', context)


def join_game(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    # user joining
    user = User.objects.get(id=request.session['user_id'])
    # game being joined
    game = Game.objects.get(id=id)
    # add user to game!
    game.participants.add(user)
    return redirect('/games')


def leave_game(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    game = Game.objects.get(id=id)
    game.participants.remove(user)
    return redirect(
        '/games')

# def edit(request, id):
    
#     context = {
#         # 'game': Game.objects.get(id=game_id),
#         'one_game': Game.objects.get(id=id),
#         # 'game': Game.objects.get(id=request.session['game_id']),
#         'creator': User.objects.get(id=request.session['user_id'])
#     }
#     return render(request, 'edit_game.html', context)

def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    # get the clicked group
    context = {
        'one_game': Game.objects.get(id=id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'edit_game.html', context)

def update(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        # game = Game.objects.get(id=request.session['id'])
        # to_update = Game.objects.get(id=id)
        # to_update.gameType = request.POST['gameType']
        # to_update.date = request.POST['date']
        # to_update.startTime = request.POST['startTime']
        # to_update.endTime = request.POST['endTime']
        # to_update.location = request.POST['location']
        # to_update.notes = request.POST['notes']
        game = Game.objects.get(id=id)
        game.gameType = request.POST['gameType']
        game.date = request.POST['date']
        game.startTime = request.POST['startTime']
        game.endTime = request.POST['endTime']
        game.location = request.POST['location']
        game.notes = request.POST['notes']
        
        Game.save()
        
        return redirect('/games/')


def delete(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        game_to_delete = Game.objects.get(id=id)
        game_to_delete.delete()
    return redirect('/games')


def catchall(request, url):
    return redirect('/')
