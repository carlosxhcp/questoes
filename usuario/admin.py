
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class AdministracaoUsuario(UserAdmin):
    model = Usuario

    list_display = (
        "email",
        "nome",
        "is_staff",
        "is_active",
    )

    ordering = ("email",)
    search_fields = ("email", "nome")

    fieldsets = (
        ("Dados da conta", {
            "fields": ("email", "password"),
        }),
        ("Dados pessoais", {
            "fields": ("nome",),
        }),
        ("Permissões", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        ("Datas", {
            "fields": ("last_login", "date_joined"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
