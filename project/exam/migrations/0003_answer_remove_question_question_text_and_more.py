# Generated by Django 5.1.1 on 2024-10-16 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_lesson_video_lesson'),
        ('exam', '0002_lesson_question_video_test_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(max_length=255)),
                ('option_4', models.CharField(max_length=255)),
                ('correct_option', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='courses.video'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.answer'),
            preserve_default=False,
        ),
    ]