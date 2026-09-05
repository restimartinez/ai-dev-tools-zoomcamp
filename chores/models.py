from django.conf import settings
from django.db import models


class FamilyMember(models.Model):
    """A household member linked 1:1 to a Django auth User."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='family_member',
    )
    is_parent = models.BooleanField(
        default=False,
        help_text='Exactly one parent manages members and tasks for the household.',
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Inactive members cannot log in or complete tasks.',
    )
    display_name = models.CharField(
        max_length=150,
        blank=True,
        help_text='Optional name shown in the app. If empty, the username is used.',
    )

    def __str__(self):
        return self.get_display_name()

    def get_display_name(self):
        """Return display_name if set, otherwise the linked user's username."""
        if self.display_name:
            return self.display_name
        return self.user.get_username()
