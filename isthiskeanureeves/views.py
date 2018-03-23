from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return index(request)
def index(request):
    context_dict = {    
    'keanuimg1': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Keanu_Reeves_2014.jpg/220px-Keanu_Reeves_2014.jpg" 
    }
    return render(request, 'isthiskeanureeves/index.html',context_dict)
    
def keanew(request):
    return HttpResponse("This is the kea-new page")
def about(request):
    context_dict = {}
    return render(request, 'isthiskeanureeves/about.html',context_dict)
    

def keanothim(request):
    return HttpResponse("This is the kea-not-him page")
def login(request):
    return HttpResponse("This is the login page")
def upload(request):
    return HttpResponse("This is the upload page")

#this needs to fully converted to work with the post <title> pages
#@login_required
def post(request,post_title_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
#wip^

#register
def register(request):

       registered = False

       if request.method == 'POST':

            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():

                    user = user_form.save()

                    user.set_password(user.password)
                    user.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user

                    if 'picture' in request.FILES:
                        profile.picture = request.FILES['picture']

                        profile.save()

                        registered = True
                    else:

                        print(user_form.errors, profile_form.errors)
       else:
           user_form = UserForm()
           profile_form = UserProfileForm()

       return render(request,
                     'isthiskeanureeves/register.html',
                     {'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered})

#login
def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
               return HttpResponse("Your isthiskeanureeves.com account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Wrong username or Wrong password.")

    else:
        return render(request, 'isthiskeanureeves/login.html', {})

@login_required
def restricted(request):
      return render(request, 'isthiskeanureeves/restricted.html', {})

    
@login_required
def user_logout(request):
         logout(request)
         return HttpResponseRedirect(reverse('index'))

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        #selects only the uploads of a particular category
        uploads = Upload.objects.filter(category=category)
        context_dict['uploads'] = uploads
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['uploads'] = None
    return render(request, 'isthiskeanureeves/category.html', context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'isthiskeanureeves/add_category.html', {'form': form})
    

