from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    verbose_name = '商品信息'

    # 加载信号量
    def ready(self):
        import goods.signals
