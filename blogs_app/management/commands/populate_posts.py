# blogs_app/management/commands/populate_posts.py
from django.core.management.base import BaseCommand
from blogs_app.models import post
from user_app.models import user
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate the post model with dummy data for existing users'

    def handle(self, *args, **kwargs):
        usernames = [
            'mpattlel0', 'bkemp1', 'cwanklin2', 'rplumbe3', 'hsantacrole4', 'jpiletic5',
            'moliveti6', 'asmewin7', 'cbartzen8', 'iaxtens9', 'bwaadenburga', 'arobroeb',
            'ahaggletonc', 'zlengthornd', 'gsuttiee', 'mwhybrowf', 'gcornboroughg',
            'sdeightonh', 'erowcliffei', 'akelleherj'
        ]

        for username in usernames:
            try:
                user_instance = user.objects.get(username=username)
                for i in range(3):  # Create 3 posts for each user
                    post_title = f'Post {i+1} by {username}'
                    post_category = random.choice(['General', 'Tech', 'Health', 'Travel', 'Education'])
                    post_content = f'This is the content of post {i+1} by {username}.'
                    new_post = post(
                        title=post_title,
                        category=post_category,
                        content=post_content,
                        date=timezone.now(),
                        written_by=user_instance
                    )
                    new_post.save()
                    self.stdout.write(self.style.SUCCESS(f'Created post: {new_post.title} for user: {username}'))
            except user.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'User not found: {username}'))
