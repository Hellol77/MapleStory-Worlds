# Generated by Django 4.1 on 2022-09-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "user_id",
                    models.CharField(max_length=17, unique=True, verbose_name="아이디"),
                ),
                ("password", models.CharField(max_length=256, verbose_name="비밀번호")),
                (
                    "email",
                    models.EmailField(
                        max_length=128, null=True, unique=True, verbose_name="이메일"
                    ),
                ),
                (
                    "hp",
                    models.IntegerField(null=True, unique=True, verbose_name="핸드폰번호"),
                ),
                ("name", models.CharField(max_length=8, null=True, verbose_name="이름")),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("3", "Lv3_해커톤참여자"),
                            ("2", "Lv2_기획단"),
                            ("1", "Lv1_관리자"),
                            ("0", "Lv0_개발자"),
                        ],
                        default=3,
                        max_length=18,
                        verbose_name="등급",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "사용자",
                "verbose_name_plural": "사용자",
                "db_table": "회원목록",
            },
        ),
    ]
