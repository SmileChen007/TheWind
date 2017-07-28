# coding:utf-8

from motorengine import Document, StringField, IntField, EmailField, URLField, FloatField, ListField


class BaseDocument(Document):
    def to_dict(self):
        data = super(Document, self).to_son()
        data['id'] = str(self._id)
        return data


class Book(BaseDocument):
    # 书籍
    novel_name = StringField()
    novel_img_url = StringField()
    novel_author = StringField()
    novel_details = StringField()
    novel_down_url = StringField()
    novel_size = StringField(default='0.0')
    novel_catalog_url = StringField()
    novel_origin = StringField()
    novel_grade = IntField(default=0, min_value=0, max_value=10)
    novel_download_count = IntField(default=0)
    novel_status_code = IntField()
    novel_scan_count = IntField(default=0)
    create_time = StringField()
    update_time = StringField()


class BookManage(BaseDocument):
    # 书籍管理
    book_amount = IntField(default=0, min_value=0)
    book_size = FloatField(default=0.00)


class BookStatus(BaseDocument):
    # 书籍状态
    book_code = IntField()
    book_status = StringField()
    extra = StringField()


class BookCategory(BaseDocument):
    # 书籍分类
    novel_category = StringField()
    category_include = StringField()


class User(BaseDocument):
    # 用户
    nickname = StringField()
    password = StringField()
    email = EmailField()
    mobile = StringField()
    gender = IntField(default=-1)
    description = StringField()
    avatar_url = StringField()
    create_time = StringField()
    up_book_amount = IntField()
    token = StringField()
    address = StringField()
    push_id = StringField()
    books = ListField(StringField())


class BookXH(Book):
    # 玄幻
    novel_category = StringField(default="xuanhuan")


class BookDS(Book):
    # 都市
    novel_category = StringField(default="dushi")


class BookXX(Book):
    # 仙侠
    novel_category = StringField(default="xianxia")


class BookLS(Book):
    # 历史
    novel_category = StringField(default="lishi")


class BookWY(Book):
    # 网游
    novel_category = StringField(default="wangyou")


class BookKH(Book):
    # 科幻
    novel_category = StringField(default="kehuan")


class BookKB(Book):
    # 恐怖
    novel_category = StringField(default="kongbu")


class BookYQ(Book):
    # 言情
    novel_category = StringField(default="yanqing")


class BookWX(Book):
    # 文学
    novel_category = StringField(default="wenxue")


class BookOther(Book):
    # 其他
    novel_category = StringField(default="other")


class BookFinish(Book):
    # 完本
    novel_category = StringField(default="wanjie")


class Recommend(Book):
    # 推荐
    novel_category = StringField(default="recommend")
