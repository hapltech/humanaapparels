from django import forms
from users.models import Department, Role, User
from django.contrib.auth.models import Permission
from unfold.forms import (
    UserChangeForm,
)


class DepartmentAdminForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["permissions"].queryset = Permission.objects.exclude(
            codename__contains="historical"
        )


class RoleAdminForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["permissions"].queryset = Permission.objects.exclude(
            codename__contains="historical"
        )


class UserAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_permissions"].queryset = Permission.objects.exclude(
            codename__contains="historical"
        )
