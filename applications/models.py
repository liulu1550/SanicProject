# coding: utf-8
from datetime import datetime

from tortoise import fields

from passlib.context import CryptContext

from utils.models import BaseModel
from utils.string_utils import generate_random_string

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    """用户表"""

    class Meta:
        table = "t_user"
        table_description = "用户表"

    mobile = fields.CharField(max_length=11, unique=True, description="用户名")
    password = fields.CharField(max_length=256, description="密码")
    status = fields.BooleanField(default=False, description="用户状态")
    authorization_token = fields.CharField(max_length=64, unique=True, description="用户唯一凭证")
    last_login = fields.DatetimeField(null=True, description="上次登录时间")

    @classmethod
    async def create_user(cls, mobile: str, password: str):
        """
        创建新用户
        :param mobile:
        :param password:
        :return:
        """
        hashed_password = pwd_context.hash(password)
        user = await cls.create(username=mobile, password=hashed_password,
                                authorization_token=generate_random_string(64))
        return user

    async def verify_password(self, plain_password: str) -> bool:
        """
        验证用户密码
        :param plain_password: 输入的密码
        :return:
        """
        return pwd_context.verify(plain_password, self.password)

    async def update_last_login(self):
        """
        更新上次登录时间
        :return:
        """
        self.last_login = datetime.now()
        await self.save()

    async def update_user_info(self, new_mobile: str = None, new_password: str = None, new_status: bool = None):
        """
        更新用户
        :param new_mobile: 新手机号
        :param new_password: 新密码
        :param new_status:  状态
        :return:
        """
        if new_mobile:
            self.mobile = new_mobile
        if new_password:
            self.password = pwd_context.hash(new_password)
        if new_status:
            self.status = new_status
        self.update_datetime = datetime.now()  # 更新日期
        await self.save()


class Test(BaseModel):
    """测试表"""

    class Meta:
        table = "t_test"
        table_description = "测试表"

    value = fields.CharField(max_length=11, unique=True, description="测试")
    user = fields.ForeignKeyField("models.User", db_constraint=False, index=True, null=False, related_name="rel_test_user", description="测试的用户id")
