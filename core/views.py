
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from .forms import PersonalDetailsForm, WorkExperienceForm, EducationForm, SkillForm
from .models import PersonalDetails, WorkExperience, Education, Skill
from django.shortcuts import render, redirect
from .forms import PersonalDetailsForm, WorkExperienceForm, EducationForm, SkillForm, ResumeForm
from .models import PersonalDetails, WorkExperience, Education, Skill
from django.contrib.auth.decorators import login_required

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log the user in after sign-up
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard View

@login_required
def dashboard_view(request):
    # Get the personal details for the logged-in user (if any)
    personal_details = PersonalDetails.objects.filter(user=request.user).first()
    work_experience = WorkExperience.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)

    # Initialize the forms for each section, using the instance if available
    personal_form = PersonalDetailsForm(instance=personal_details)
    work_form = WorkExperienceForm()
    education_form = EducationForm()
    skill_form = SkillForm()

    # Process the 'ResumeForm' for saving the resume data (if it is submitted)
    if request.method == 'POST':
        # Create a ResumeForm instance for handling the resume form
        resume_form = ResumeForm(request.POST)
        if resume_form.is_valid():
            resume_form.save()  # Save the resume data to the database
            return redirect('resume_success')  # Redirect to a success page or another page

    else:
        resume_form = ResumeForm()  # Show an empty form if no data is posted

    # Return the dashboard page with all forms and related data
    return render(request, 'core/dashboard.html', {
        'personal_form': personal_form,
        'work_form': work_form,
        'education_form': education_form,
        'skill_form': skill_form,
        'resume_form': resume_form,  # Include the resume form in the context
        'work_experience': work_experience,
        'education': education,
        'skills': skills,
    })


# Resume View
@login_required
def resume_view(request):
    personal_details = PersonalDetails.objects.filter(user=request.user).first()
    work_experience = WorkExperience.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)

    return render(request, 'core/resume.html', {
        'personal_details': personal_details,
        'work_experience': work_experience,
        'education': education,
        'skills': skills,
    })


# Generate PDF View
@login_required
def generate_pdf(request):
    personal_details = PersonalDetails.objects.filter(user=request.user).first()
    work_experience = WorkExperience.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)

    if not personal_details:
        messages.error(request, "Please complete your personal details before generating a PDF.")
        return redirect('dashboard')

    html_content = render_to_string('core/resume.html', {
        'personal_details': personal_details,
        'work_experience': work_experience,
        'education': education,
        'skills': skills,
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', content_type='text/plain')

    return response


# CRUD for Work Experience
@login_required
def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.save()
            messages.success(request, 'Work experience added successfully!')
        else:
            messages.error(request, 'Failed to add work experience. Please correct the errors.')
    return redirect('dashboard')


@login_required
def edit_work_experience(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work experience updated successfully!')
            return redirect('dashboard')
    else:
        form = WorkExperienceForm(instance=work)
    return render(request, 'core/edit_work_experience.html', {'form': form})


@login_required
def delete_work_experience(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    work.delete()
    messages.success(request, 'Work experience deleted successfully!')
    return redirect('dashboard')


# CRUD for Education
@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            messages.success(request, 'Education added successfully!')
        else:
            messages.error(request, 'Failed to add education.')
    return redirect('dashboard')


@login_required
def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully!')
            return redirect('dashboard')
    else:
        form = EducationForm(instance=education)
    return render(request, 'core/edit_education.html', {'form': form})


@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    education.delete()
    messages.success(request, 'Education deleted successfully!')
    return redirect('dashboard')


# CRUD for Skills
@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
        else:
            messages.error(request, 'Failed to add skill.')
    return redirect('dashboard')



@login_required
def edit_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'core/edit_skill.html', {'form': form})


@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('dashboard')


# CRUD for Personal Details
@login_required
def save_personal_details(request):
    if request.method == 'POST':
        personal_details = PersonalDetails.objects.filter(user=request.user).first()
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        
        if form.is_valid():
            personal_details = form.save(commit=False)  # Save without committing to DB yet
            personal_details.user = request.user  # Set the user to the logged-in user
            personal_details.save()  # Save the object to the database
            messages.success(request, 'Personal details updated successfully!')
        else:
            messages.error(request, 'Error updating personal details.')
    return redirect('dashboard')

@login_required
def edit_personal_details(request):
    personal_details = PersonalDetails.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal details updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error updating your personal details. Please try again.')
    else:
        form = PersonalDetailsForm(instance=personal_details)

    return render(request, 'core/edit_personal_details.html', {'form': form})

@login_required
def delete_personal_details(request):
    personal_details = PersonalDetails.objects.filter(user=request.user).first()
    if personal_details:
        personal_details.delete()
        messages.success(request, 'Personal details deleted successfully!')
    else:
        messages.error(request, 'No personal details found to delete.')
    return redirect('dashboard')
