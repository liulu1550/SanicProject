from tortoise import Model, fields


class BaseModel(Model):
    """
    基础模型
    """
    class Meta:
        table = "t_base"
        table_description = "基础模型"
    id = fields.BigIntField(pk=True, description="表id")
    create_datetime = fields.DatetimeField(null=False, auto_now_add=True, description="创建时间")
    update_datetime = fields.DatetimeField(null=False, auto_now=True, description="更新时间")


