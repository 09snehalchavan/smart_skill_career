from django.shortcuts import render, HttpResponse

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, ProfileForm, UserSkillForm, CareerGoalForm
from .models import Profile, UserSkill, CareerGoal, Career, CareerSkill, Course

def root_page(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(
        request,
        'home.html'
    )


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.create(
                user=user,
                full_name=user.username,
                phone='Fill Data',
                education='Fill Data',
                college='Fill Data',
                location='Fill Data',
            )

            login(request, user)

            messages.success(
                request,
                'Registration successful! Welcome to Smart Career.'
            )

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )



@login_required
def dashboard_view(request):

    profile = get_object_or_404(
        Profile,
        user=request.user
    )

    career_goal = CareerGoal.objects.filter(
        user=request.user
    ).first()

    total_required = 0
    total_matched = 0
    total_missing = 0
    match_percentage = 0
    recommended_courses_count = 0

    if career_goal:

        career = Career.objects.filter(
            name=career_goal.target_role,
            is_active=True
        ).first()

        if career:

            required_skills = CareerSkill.objects.filter(
                career=career
            ).select_related('skill')

            user_skills = UserSkill.objects.filter(
                user=request.user
            ).select_related('skill')

            user_skill_names = {
                user_skill.skill.name.strip().lower()
                for user_skill in user_skills
            }

            total_required = required_skills.count()

            missing_skills = []

            for required_skill in required_skills:

                skill_name = required_skill.skill.name.strip().lower()

                if skill_name in user_skill_names:
                    total_matched += 1
                else:
                    missing_skills.append(required_skill)

            total_missing = len(missing_skills)

            if total_required > 0:
                match_percentage = round(
                    (total_matched / total_required) * 100,
                    1
                )

            recommended_courses_count = Course.objects.filter(
                skill__in=[
                    item.skill for item in missing_skills
                ],
                is_active=True
            ).count()

    context = {
        'profile': profile,
        'career_goal': career_goal,
        'total_required': total_required,
        'total_matched': total_matched,
        'total_missing': total_missing,
        'match_percentage': match_percentage,
        'recommended_courses_count': recommended_courses_count,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )

@login_required
def profile_view(request):

    profile = get_object_or_404(
        Profile,
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Profile updated successfully.'
            )

            return redirect('profile')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'profile/profile.html',
        {
            'form': form,
            'profile': profile,
        }
    )


@login_required
def my_skills_view(request):

    user_skills = UserSkill.objects.filter(
        user=request.user
    ).select_related('skill')

    return render(
        request,
        'skills/my_skills.html',
        {
            'user_skills': user_skills
        }
    )


@login_required
def add_skill_view(request):

    if request.method == 'POST':

        form = UserSkillForm(request.POST)

        if form.is_valid():

            user_skill = form.save(commit=False)

            user_skill.user = request.user

            user_skill.save()

            messages.success(
                request,
                'Skill added successfully.'
            )

            return redirect('my_skills')

    else:

        form = UserSkillForm()

    return render(
        request,
        'skills/add_skills.html',
        {
            'form': form
        }
    )


@login_required
def edit_skill_view(request, skill_id):

    user_skill = UserSkill.objects.get(
        id=skill_id,
        user=request.user
    )

    if request.method == 'POST':

        form = UserSkillForm(
            request.POST,
            instance=user_skill
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Skill updated successfully.'
            )

            return redirect('my_skills')

    else:

        form = UserSkillForm(
            instance=user_skill
        )

    return render(
        request,
        'skills/edit_skill.html',
        {
            'form': form
        }
    )

@login_required
def delete_skill_view(request, skill_id):

    user_skill = UserSkill.objects.get(
        id=skill_id,
        user=request.user
    )

    if request.method == 'POST':

        user_skill.delete()

        messages.success(
            request,
            'Skill deleted successfully.'
        )

        return redirect('my_skills')

    return render(
        request,
        'skills/delete_skill.html',
        {
            'user_skill': user_skill
        }
    )


@login_required
def career_goal_view(request):

    try:
        career_goal = CareerGoal.objects.get(
            user=request.user
        )
    except CareerGoal.DoesNotExist:
        career_goal = None

    if request.method == 'POST':

        form = CareerGoalForm(
            request.POST,
            instance=career_goal
        )

        if form.is_valid():

            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()

            messages.success(
                request,
                'Career goal saved successfully.'
            )

            return redirect('career_goal')

    else:

        form = CareerGoalForm(
            instance=career_goal
        )

    return render(
        request,
        'career/career_goal.html',
        {
            'form': form,
            'career_goal': career_goal
        }
    )

@login_required
def skill_gap_view(request):

    career_goal = CareerGoal.objects.filter(
        user=request.user
    ).first()

    if not career_goal:
        return redirect('career_goal')

    career = Career.objects.filter(
        name=career_goal.target_role,
        is_active=True
    ).first()

    if not career:
        return render(
            request,
            'skills/skill_gap.html',
            {
                'career_goal': career_goal,
                'career': None,
                'error': 'No career found for your career goal.'
            }
        )

    required_skills = CareerSkill.objects.filter(
        career=career
    )

    user_skills = UserSkill.objects.filter(
        user=request.user
    ).select_related('skill')

    user_skill_names = {
        user_skill.skill.name.strip().lower()
        for user_skill in user_skills
    }

    matched_skills = []
    missing_skills = []

    for required_skill in required_skills:

        skill_name = required_skill.skill.name.strip()

        if skill_name.lower() in user_skill_names:
            matched_skills.append(required_skill)
        else:
            missing_skills.append(required_skill)

    # Recommended courses for missing skills
    recommended_courses = []

    for missing_skill in missing_skills:

        courses = Course.objects.filter(
            skill=missing_skill.skill,
            is_active=True
        )

        recommended_courses.extend(courses)

    # Skill match calculation
    total_required = required_skills.count()
    total_matched = len(matched_skills)

    if total_required > 0:
        match_percentage = round(
            (total_matched / total_required) * 100,
            1
        )
    else:
        match_percentage = 0

    context = {
        'career_goal': career_goal,
        'career': career,
        'required_skills': required_skills,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'recommended_courses': recommended_courses,
        'total_required': total_required,
        'total_matched': total_matched,
        'match_percentage': match_percentage,
    }

    return render(
        request,
        'skills/skill_gap.html',
        context
    )


@login_required
def career_recommendation_view(request):

    user_skills = UserSkill.objects.filter(
        user=request.user
    ).select_related('skill')

    user_skill_names = {
        user_skill.skill.name.strip().lower()
        for user_skill in user_skills
    }

    careers = Career.objects.filter(
        is_active=True
    )

    recommendations = []

    for career in careers:

        required_skills = CareerSkill.objects.filter(
            career=career
        ).select_related('skill')

        total_required = required_skills.count()
        total_matched = 0

        for required_skill in required_skills:

            skill_name = required_skill.skill.name.strip().lower()

            if skill_name in user_skill_names:
                total_matched += 1

        if total_required > 0:
            match_percentage = round(
                (total_matched / total_required) * 100,
                1
            )
        else:
            match_percentage = 0

        recommendations.append({
            'career': career,
            'total_required': total_required,
            'total_matched': total_matched,
            'match_percentage': match_percentage,
        })

    recommendations.sort(
        key=lambda x: x['match_percentage'],
        reverse=True
    )

    context = {
        'recommendations': recommendations,
    }

    return render(
        request,
        'career/career_recommendation.html',
        context
    )