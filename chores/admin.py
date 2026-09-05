from django.contrib import admin

from .models import FamilyMember


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    """
    Manage family members, including the first parent.

    Bootstrap tip: create a User (e.g. via createsuperuser or Users admin),
    then add a FamilyMember here with is_parent=True and is_active=True.
    """

    list_display = ('get_display_name', 'user', 'is_parent', 'is_active')
    list_filter = ('is_parent', 'is_active')
    search_fields = ('display_name', 'user__username')
    autocomplete_fields = ('user',)
    ordering = ('user__username',)
