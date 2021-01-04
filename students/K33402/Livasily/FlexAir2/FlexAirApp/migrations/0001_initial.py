# Generated by Django 3.1.4 on 2021-01-03 15:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airaport', models.CharField(max_length=30, verbose_name='Аэропорт')),
            ],
        ),
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.airport', verbose_name='Прилет')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.airport', verbose_name='отлет')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('Transit', models.BooleanField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.airline')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('passport', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateDeparture', models.DateTimeField()),
                ('dateArrival', models.DateTimeField()),
                ('distance', models.PositiveIntegerField()),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Прилет', to='FlexAirApp.arrival')),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='отлет', to='FlexAirApp.departure')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('countPlace', models.PositiveSmallIntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('1', 'Pilot'), ('2', 'SecondPilot'), ('3', 'Navigator')], max_length=1, verbose_name='должность')),
                ('Experience', models.PositiveSmallIntegerField()),
                ('board', models.ManyToManyField(to='FlexAirApp.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilot', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlightAttendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education', models.CharField(choices=[('I', 'ITMO'), ('S', 'SPBGU'), ('D', 'DVFU')], max_length=1, verbose_name='Об')),
                ('Experience', models.PositiveSmallIntegerField()),
                ('board', models.ManyToManyField(to='FlexAirApp.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='courses',
            field=models.ManyToManyField(to='FlexAirApp.Route'),
        ),
        migrations.AddField(
            model_name='board',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.flight'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.city'),
        ),
        migrations.AddField(
            model_name='airport',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexAirApp.airline', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='airline',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='airport',
            unique_together={('company', 'city', 'airaport')},
        ),
    ]