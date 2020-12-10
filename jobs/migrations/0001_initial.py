# Generated by Django 3.1.3 on 2020-12-10 06:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_username', models.CharField(max_length=100)),
                ('emp_mobile', models.IntegerField()),
                ('emp_address', models.CharField(max_length=200)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_name', models.CharField(max_length=100)),
                ('j_type', models.CharField(max_length=100)),
                ('j_desc', models.TextField()),
                ('j_emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.employee')),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=100)),
                ('r_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=100)),
                ('s_type', models.CharField(max_length=100)),
                ('s_desc', models.TextField()),
                ('s_job_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
        migrations.CreateModel(
            name='permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_name', models.CharField(max_length=100)),
                ('per_module', models.CharField(max_length=100)),
                ('per_role_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Joblist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default1.jpg', upload_to='profile_pics')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('i_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('desc', models.TextField()),
                ('job_joblist', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_title', models.CharField(max_length=100)),
                ('i_type', models.CharField(max_length=100)),
                ('i_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_desc', models.TextField()),
                ('i_job_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
        migrations.CreateModel(
            name='call_letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_title', models.CharField(max_length=100)),
                ('cl_type', models.CharField(max_length=100)),
                ('cl_desc', models.TextField()),
                ('cl_emp_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.employee')),
                ('cl_job_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
