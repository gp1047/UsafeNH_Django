from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from collection.forms import CollegeForm
from collection.models import College, Hospital
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


# the rewritten view!
def index(request):
    colleges = College.objects.all()
    hospitals = Hospital.objects.all()

    return render(request, 'index.html', {
        'colleges': colleges,
        'hospitals': hospitals,
    })

# our new view
def thing_detail(request, slug,):
    # grab the object...
    college = College.objects.get(slug=slug)
    hospital = Hospital.objects.all()
    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'college': college,
        'hospital': hospital,
    })

# add below your thing_detail view
@login_required
def edit_thing(request, slug):
    # grab the object
    college = College.objects.get(slug=slug)

    if college.user != request.user:
        raise Http404

    # set the form we're using
    form_class = CollegeForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=college)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=college.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=college)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'college': college,
        'form': form,
    })

def create_thing(request):
    form_class = CollegeForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            college = form.save(commit=False)

            # set the additional details
            college.user = request.user
            college.slug = slugify(college.name)

            # save the object
            college.save()

            # redirect to our newly created thing
            return redirect('thing_detail', slug=college.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'things/create_thing.html', {
        'form': form,
    })
