from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(default='null', unique=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('observation_id', models.AutoField(primary_key=True, serialize=False)),
                ('observation_name', models.CharField(default='null', unique=True)),
            ],
            options={
                'db_table': 'observations',
            },
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(null=True)),
                ('last_name', models.CharField(null=True)),
                ('username', models.CharField(default='null', unique=True)),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('variable_id', models.AutoField(primary_key=True, serialize=False)),
                ('variable_name', models.CharField(default='null')),
                ('channel', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'variables',
                'unique_together': {('variable_name', 'channel')},
            },
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('experiment_id', models.AutoField(primary_key=True, serialize=False)),
                ('experiment_name', models.CharField(default='null')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owners')),
            ],
            options={
                'db_table': 'experiments',
                'unique_together': {('experiment_name', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('plot_id', models.AutoField(primary_key=True, serialize=False)),
                ('div', models.CharField(blank=True, null=True)),
                ('script', models.CharField(blank=True, null=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.experiments')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.groups')),
                ('observation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.observations')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.variables')),
            ],
            options={
                'db_table': 'plots',
                'unique_together': {('experiment', 'group', 'observation', 'variable')},
            },
        ),
    ]
