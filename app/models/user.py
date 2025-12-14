from tortoise import fields, models

class UserModel(models.Model):
    id = fields.IntField(pk=True, auto_create=True)
    login_id = fields.CharField(unique=True, max_length=255)
    email = fields.CharField(unique=True, max_length=255)
    nickname = fields.CharField(unique=True, max_length=255)
    hashed_password = fields.CharField(max_length=128)
    birthday = fields.DateField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    admin = fields.BooleanField(default=False)

    class Meta:
        table = "user"

    def __str__(self):
        return self.login_id