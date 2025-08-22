from django.db import models

class Program(models.Model):
    MORNING = 'AM'
    AFTERNOON = 'PM'
    SESSION_CHOICES = [
        (MORNING, '午前の部'),
        (AFTERNOON, '午後の部'),
    ]
    
    # 午前・午後
    session = models.CharField(max_length=2, choices=SESSION_CHOICES)
    
    # プログラム番号
    number = models.PositiveIntegerField()
    
    # プログラム名
    name = models.CharField(max_length=100)
    
    # 出場学年（複数選択）
    GRADE_CHOICES = [
        ('中1', '中学1年'),
        ('中2', '中学2年'),
        ('中3', '中学3年'),
        ('高1', '高校1年'),
        ('高2', '高校2年'),
        ('高3', '高校3年'),
        ('全学年', '全学年'),
        ('全団', '全団'),
    ]
    grades = models.JSONField(default=list)  # 複数選択をJSONで保存
    
    # 説明文
    description = models.TextField(blank=True)
    
    # 画像
    image = models.ImageField(upload_to='program_images/', blank=True, null=True)

    class Meta:
        ordering = ['session', 'number']  # デフォルト並び順

    def __str__(self):
        return f"{self.session} {self.number} {self.name}"
