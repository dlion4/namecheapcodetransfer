# Generated by Django 4.2.4 on 2023-09-17 12:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("is_editors_choice", models.BooleanField(default=False)),
                ("slug", models.SlugField(blank=True, max_length=100, null=True)),
                ("content", ckeditor.fields.RichTextField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "summary",
                    models.TextField(
                        blank=True,
                        help_text="summary of the blog post",
                        max_length=300,
                        null=True,
                    ),
                ),
                ("image", models.ImageField(upload_to="posts/")),
                ("views", models.IntegerField(default=1)),
                (
                    "bg_image",
                    models.ImageField(blank=True, null=True, upload_to="bg_posts/"),
                ),
                ("is_approved", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="post_tags", to="category.tag"
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topic_posts",
                        to="category.topic",
                    ),
                ),
                (
                    "writer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="post_author",
                        to="accounts.profile",
                    ),
                ),
            ],
            options={
                "get_latest_by": "createdAt",
            },
        ),
        migrations.CreateModel(
            name="PostImage",
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
                ("slider", models.ImageField(upload_to="images/slider/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_post_image",
                        to="posts.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostComment",
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
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("full_name", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("postedAt", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comments",
                        to="posts.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommentReply",
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
                ("reply", models.TextField()),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_reply",
                        to="posts.postcomment",
                    ),
                ),
            ],
        ),
    ]
