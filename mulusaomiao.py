# coding=utf-8
import requests
class Mulu:
    def __init__(self,url,file_name):
        self.file_name = file_name
        self.url = url



    def get_dict(self,file_name):
        """
        读取字典文件内容
        返回字典值

        """
        with open(file_name, "r") as f:
            url_dict = f.read().splitlines()
            return url_dict


    def get_url(self,url,url_dict):
        """
        获取url并进行拼接URL扫描该网站下的所有目录
        """

        url_list = []
        for i in range(0, len(url_dict)):
            url_1 = "http://{}/{}".format(url, url_dict[i])
            # print(url_1)
            res = requests.get(url_1)
            # print(res.status_code)
            if res.status_code == 200 or res.status_code == 403:
                url_list.append(url_1)
        return url_list


if __name__ == '__main__':
    url =input("请输入域名:")
    url_dict = Mulu.get_dict(Mulu, "mu1.txt")
    mulu = Mulu.get_url(Mulu, url, url_dict)
    print(mulu)

