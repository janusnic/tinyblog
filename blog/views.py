from django.shortcuts import render

from django.http import HttpResponse 
from blog.models import Category, Post
from blog.forms import UserForm, UserProfileForm
import datetime

def index(request):
	category_list = Category.objects.order_by('name')
	post_list = Post.objects.order_by('title')
	context_dict = {'categories': category_list, 'posts': post_list}
	return render(request, 'blog/index.html', context_dict)

def view(request, postslug):
	post = Post.objects.get(slug=postslug)
	context = {'post': post}
	return render_to_response('blog/singlepost.html', context)

def category(reqeust, categoryslug):
	cat = Category.objects.get(slug=categoryslug)
	posts = Post.objects.filter(categoty=cat)
	context = {'posts': posts}
	return render_to_response('blog/singlecategory.html', context)

	
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'blog/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )