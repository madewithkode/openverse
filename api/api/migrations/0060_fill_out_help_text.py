# Generated by Django 4.2.11 on 2024-04-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_userpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='alt_files',
            field=models.JSONField(blank=True, help_text='\nJSON object containing information on alternative audio files. Each object\nis expected to contain:\n\n- `url`: URL reference to the file\n- `filesize`: File size in bytes\n- `filetype`: Extension of the file\n- `bit_rate`: Bitrate of the file in bits/second\n- `sample_rate`: Sample rate of the file in bits/second\n', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='last_synced_with_source',
            field=models.DateTimeField(blank=True, db_index=True, help_text='The date the media was last updated from the upstream source.', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='meta_data',
            field=models.JSONField(blank=True, help_text='\nJSON object containing extra data about the media item. No fields are expected,\nbut if the `license_url` field is available, it will be used for determining\nthe license URL for the media item. The `description` field, if available, is\nalso indexed into Elasticsearch and as a search field on queries.\n', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='removed_from_source',
            field=models.BooleanField(default=False, help_text='Whether the media has been removed from the upstream source.'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='tags',
            field=models.JSONField(blank=True, help_text='\nJSON array of objects containing tags for the media. Each tag object\nis expected to have:\n\n- `name`: The tag itself (e.g. "dog")\n- `provider`: The source of the tag\n- `accuracy`: If the tag was added using a machine-labeler, the confidence\nfor that label expressed as a value between 0 and 1.\n\nNote that only `name` and `accuracy` are presently surfaced in API results.\n', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, help_text='Vestigial field, purpose unknown.', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='watermarked',
            field=models.BooleanField(blank=True, help_text='Whether the media contains a watermark. Not currently leveraged.', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='last_synced_with_source',
            field=models.DateTimeField(blank=True, db_index=True, help_text='The date the media was last updated from the upstream source.', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='meta_data',
            field=models.JSONField(blank=True, help_text='\nJSON object containing extra data about the media item. No fields are expected,\nbut if the `license_url` field is available, it will be used for determining\nthe license URL for the media item. The `description` field, if available, is\nalso indexed into Elasticsearch and as a search field on queries.\n', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='removed_from_source',
            field=models.BooleanField(default=False, help_text='Whether the media has been removed from the upstream source.'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.JSONField(blank=True, help_text='\nJSON array of objects containing tags for the media. Each tag object\nis expected to have:\n\n- `name`: The tag itself (e.g. "dog")\n- `provider`: The source of the tag\n- `accuracy`: If the tag was added using a machine-labeler, the confidence\nfor that label expressed as a value between 0 and 1.\n\nNote that only `name` and `accuracy` are presently surfaced in API results.\n', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, help_text='Vestigial field, purpose unknown.', null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='watermarked',
            field=models.BooleanField(blank=True, help_text='Whether the media contains a watermark. Not currently leveraged.', null=True),
        ),
    ]
