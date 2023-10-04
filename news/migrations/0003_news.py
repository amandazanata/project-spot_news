from django.db import migrations, models
import django.db.models.deletion
import news.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[news.models.validators.validate_title],
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="img/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.users",
                    ),
                ),
                ("categories", models.ManyToManyField(to="news.categories")),
            ],
        )
    ]
