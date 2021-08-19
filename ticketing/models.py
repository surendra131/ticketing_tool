from django.db import models


# Create your models here
class Project(models.Model):
    '''Porject provides a way to link issues'''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here
class Sprint(models.Model):
    '''Sprint model to handle sprints associated with Project'''
    start = models.DateField()
    end = models.DateField()
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Issue(models.Model):
    '''Issue/Story/Epic/Task support model'''
    IssueStatus = models.TextChoices("IssueStatus", "Open InProgress CodeReview Completed Close")
    IssueType = models.TextChoices("IssueType", "Issue Story Epic Task")

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=IssueType.choices, default="Issue")
    status = models.CharField(max_length=10, choices=IssueStatus.choices, default="Open")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True, related_name='sprints')
    assignee = models.CharField(max_length=50, null=True, blank=True)
    labels = models.CharField(max_length=50, null=True, blank=True)
    watchers = models.CharField(max_length=50, null=True, blank=True)
    estimated_time = models.TimeField(auto_now=False, null=True, blank=True, auto_now_add=False)
    logged_time = models.TimeField(auto_now=False, null=True, blank=True, auto_now_add=False)
    reporter = models.CharField(max_length=50)

    def __str__(self):
        return self.project.name + '-' + str(self.id)


