
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class GerenciadorUsuario(BaseUserManager):
    """Gerencia a criação de usuários usando o e-mail."""

    use_in_migrations = True

    def create_user(self, email, password=None, **campos):
        if not email:
            raise ValueError("O e-mail é obrigatório.")

        email = self.normalize_email(email).strip().lower()
        usuario = self.model(email=email, **campos)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password=None, **campos):
        campos.setdefault("is_staff", True)
        campos.setdefault("is_superuser", True)
        campos.setdefault("is_active", True)

        if campos.get("is_staff") is not True:
            raise ValueError("O administrador precisa ter is_staff=True.")

        if campos.get("is_superuser") is not True:
            raise ValueError(
                "O administrador precisa ter is_superuser=True."
            )

        return self.create_user(email, password, **campos)


class Usuario(AbstractUser):
    username = None

    email = models.EmailField(
        "e-mail",
        unique=True,
    )

    nome = models.CharField(
        "nome completo",
        max_length=150,
        blank=True,
    )

    objects = GerenciadorUsuario()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.email
