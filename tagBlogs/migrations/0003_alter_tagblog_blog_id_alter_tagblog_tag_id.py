# Generated by Django 4.1.2 on 2022-11-19 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blog_date_posted_remove_blog_likes'),
        ('tags', '0001_initial'),
        ('tagBlogs', '0002_alter_tagblog_blog_id_alter_tagblog_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagblog',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogs.blog'),
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.tag'),
        ),
    ]
