from django.db import models

class UserInput(models.Model):
    user_name = models.CharField(max_length=100)
    symptoms = models.TextField()
    stress_level = models.IntegerField(choices=[(i, i) for i in range(1, 11)])  # Scale 1-10
    recommendations = models.TextField(blank=True)

    def save_recommendations(self):
        if self.stress_level <= 3:
            self.recommendations = "Try mindfulness and relaxation exercises like deep breathing."
        elif self.stress_level <= 7:
            self.recommendations = "Consider talking to a therapist or practicing grounding techniques."
        else:
            self.recommendations = "It's important to reach out to a mental health professional for immediate support."
        self.save()
