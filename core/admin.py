from django.contrib import admin

from .models import (
    Profile, Skill, UserSkill, Career, CareerSkill, UserCareerGoal, Assessment, Question, AssessmentQuestion, CareerRecommendation, LearningResource, LearningProgress, Course,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'education',
        'college',
        'location',
    )
    search_fields = (
        'user__username',
        'full_name',
        'college',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'is_active',
        'created_at',
    )
    search_fields = ('name',)
    list_filter = ('category', 'is_active')


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'skill',
        'proficiency',
        'years_of_experience',
        'self_rating',
        'is_verified',
    )
    search_fields = (
        'user__username',
        'skill__name',
    )
    list_filter = (
        'proficiency',
        'is_verified',
    )


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'demand_level',
        'average_salary',
        'is_active',
    )
    search_fields = ('name',)
    list_filter = ('demand_level', 'is_active')


@admin.register(CareerSkill)
class CareerSkillAdmin(admin.ModelAdmin):
    list_display = (
        'career',
        'skill',
        'required_proficiency',
        'importance',
    )
    search_fields = (
        'career__name',
        'skill__name',
    )
    list_filter = (
        'importance',
        'required_proficiency',
    )


@admin.register(UserCareerGoal)
class UserCareerGoalAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'career',
        'priority',
        'target_date',
        'status',
    )
    search_fields = (
        'user__username',
        'career__name',
    )
    list_filter = ('status',)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'skill',
        'score',
        'total_questions',
        'percentage',
        'level',
        'completed_at',
    )
    search_fields = (
        'user__username',
        'skill__name',
    )
    list_filter = (
        'skill',
        'level',
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'skill',
        'difficulty',
        'is_active',
    )
    search_fields = (
        'question_text',
        'skill__name',
    )
    list_filter = (
        'skill',
        'difficulty',
        'is_active',
    )


@admin.register(AssessmentQuestion)
class AssessmentQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'assessment',
        'question',
        'selected_answer',
        'is_correct',
    )
    list_filter = ('is_correct',)


@admin.register(CareerRecommendation)
class CareerRecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'career',
        'match_percentage',
        'is_recommended',
        'generated_at',
    )
    search_fields = (
        'user__username',
        'career__name',
    )
    list_filter = ('is_recommended',)


@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'skill',
        'resource_type',
        'difficulty',
        'is_active',
    )
    search_fields = (
        'title',
        'skill__name',
    )
    list_filter = (
        'resource_type',
        'difficulty',
        'is_active',
    )


@admin.register(LearningProgress)
class LearningProgressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'resource',
        'progress_percentage',
        'status',
        'updated_at',
    )
    search_fields = (
        'user__username',
        'resource__title',
    )
    list_filter = ('status',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'skill',
        'platform',
        'level',
        'duration',
        'is_active',
    )

    list_filter = (
        'level',
        'platform',
        'is_active',
    )

    search_fields = (
        'name',
        'skill__name',
    )