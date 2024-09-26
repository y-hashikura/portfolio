from django.core.management.base import BaseCommand
from django.apps import apps
import csv
import os

class Command(BaseCommand):
    help = 'Export all models data to CSV files'

    def handle(self, *args, **kwargs):
        # 出力先ディレクトリ
        output_dir = 'exported_data'
        os.makedirs(output_dir, exist_ok=True)

        # アプリケーションのすべてのモデルを取得
        for model in apps.get_models():
            model_name = model._meta.model_name
            file_path = os.path.join(output_dir, f'{model_name}.csv')

            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # ヘッダー行の書き込み
                writer.writerow([field.name for field in model._meta.fields])
                # 各レコードの書き込み
                for obj in model.objects.all():
                    writer.writerow([getattr(obj, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS('All data exported successfully!'))