from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# ============================================================
# 1. USER PROFILE
# ============================================================

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# ============================================================
# 2. SKILL
# ============================================================

class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
        ('soft_skill', 'Soft Skill'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ============================================================
# 3. USER SKILL
# User <----> Skill through UserSkill
# ============================================================

class UserSkill(models.Model):

    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='skills'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='users'
    )

    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES
    )

    years_of_experience = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0
    )

    self_rating = models.PositiveIntegerField(
        default=1
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'skill'],
                name='unique_user_skill'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"


# ============================================================
# 4. CAREER
# ============================================================

class Career(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    description = models.TextField()

    average_salary = models.CharField(
        max_length=100,
        blank=True
    )

    demand_level = models.CharField(
        max_length=50,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ============================================================
# 5. CAREER SKILL
# Career <----> Skill through CareerSkill
# ============================================================

class CareerSkill(models.Model):

    IMPORTANCE_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name='required_skills'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='career_requirements'
    )

    required_proficiency = models.CharField(
        max_length=20,
        choices=UserSkill.PROFICIENCY_CHOICES
    )

    importance = models.CharField(
        max_length=10,
        choices=IMPORTANCE_CHOICES
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['career', 'skill'],
                name='unique_career_skill'
            )
        ]

    def __str__(self):
        return f"{self.career.name} - {self.skill.name}"


# ============================================================
# 6. USER CAREER GOAL
# User <----> Career through UserCareerGoal
# ============================================================

class UserCareerGoal(models.Model):

    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='career_goals'
    )

    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name='interested_users'
    )

    priority = models.PositiveIntegerField(
        default=1
    )

    target_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planned'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'career'],
                name='unique_user_career_goal'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.career.name}"


# ============================================================
# 7. ASSESSMENT
# ============================================================

class Assessment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assessments'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='assessments'
    )

    score = models.PositiveIntegerField(default=0)

    total_questions = models.PositiveIntegerField(default=0)

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    level = models.CharField(
        max_length=20,
        blank=True
    )

    started_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"


# ============================================================
# 8. QUESTION
# ============================================================

class Question(models.Model):

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        ]
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question_text[:50]


# ============================================================
# 9. ASSESSMENT QUESTION
# Assessment <----> Question
# ============================================================

class AssessmentQuestion(models.Model):

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name='assessment_questions'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='assessment_questions'
    )

    selected_answer = models.CharField(
        max_length=1,
        blank=True
    )

    is_correct = models.BooleanField(
        default=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['assessment', 'question'],
                name='unique_assessment_question'
            )
        ]

    def __str__(self):
        return f"{self.assessment} - {self.question.id}"


# ============================================================
# 10. CAREER RECOMMENDATION
# ============================================================

class CareerRecommendation(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='career_recommendations'
    )

    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name='recommendations'
    )

    match_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    matched_skills = models.JSONField(
        default=list
    )

    missing_skills = models.JSONField(
        default=list
    )

    is_recommended = models.BooleanField(
        default=False
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.career.name} - "
            f"{self.match_percentage}%"
        )


# ============================================================
# 11. LEARNING RESOURCE
# ============================================================

class LearningResource(models.Model):

    RESOURCE_TYPES = [
        ('course', 'Course'),
        ('video', 'Video'),
        ('article', 'Article'),
        ('documentation', 'Documentation'),
        ('practice', 'Practice'),
    ]

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='learning_resources'
    )

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPES
    )

    url = models.URLField()

    difficulty = models.CharField(
        max_length=20,
        blank=True
    )

    duration = models.CharField(
        max_length=50,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ============================================================
# 12. LEARNING PROGRESS
# ============================================================

class LearningProgress(models.Model):

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='learning_progress'
    )

    resource = models.ForeignKey(
        LearningResource,
        on_delete=models.CASCADE,
        related_name='user_progress'
    )

    progress_percentage = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started'
    )

    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'resource'],
                name='unique_learning_progress'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.resource.title}"



class CareerGoal(models.Model):

    EXPERIENCE_LEVELS = [
        ('Fresher', 'Fresher'),
        ('0-1 Years', '0-1 Years'),
        ('1-3 Years', '1-3 Years'),
        ('3+ Years', '3+ Years'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    target_role = models.CharField(
        max_length=100
    )

    experience_level = models.CharField(
        max_length=50,
        choices=EXPERIENCE_LEVELS
    )

    preferred_domain = models.CharField(
        max_length=100
    )

    target_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    target_timeline = models.PositiveIntegerField(
        help_text="Timeline in months"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.target_role}"


class Course(models.Model):

    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    description = models.TextField(blank=True)

    platform = models.CharField(max_length=100)

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner'
    )

    duration = models.CharField(
        max_length=50,
        blank=True
    )

    course_url = models.URLField(
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name