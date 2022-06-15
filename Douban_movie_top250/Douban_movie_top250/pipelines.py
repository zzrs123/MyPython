from scrapy.pipelines.images import ImagesPipeline  # scrapyͼƬ������
from scrapy import Request
from scrapy.exceptions import DropItem


class DoubanMovieTop250Pipeline(ImagesPipeline):
    # ��������ͼƬ
    def get_media_requests(self, item, info):
        yield Request(item['pic_link'], meta={'name': item['name']})

    def item_completed(self, results, item, info):
        # �������ؽ�����޳�����ʧ�ܵ�ͼƬ
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # ��дfile_path��������ͼƬ��ԭ�������ƺ͸�ʽ���б���
    def file_path(self, request, response=None, info=None):
        name = request.meta['name']  # ��������meta���ݹ�����ͼƬ����
        file_name = name + '.jpg'    # ���ͼƬ��׺��
        return file_name