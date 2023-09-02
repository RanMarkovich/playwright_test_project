class NetworkListener:
    __traffic = []

    def __init__(self, page=None):
        self.page = page

    @property
    def network_traffic(self):
        return self.__traffic

    def subscribe_to_network_traffic(self):
        """helper method in test setup to fetch all network traffic"""
        self.page.on("request", lambda request: self.__store_traffic((">>", request.method, request.url, request.post_data_json)))
        self.page.on("response", lambda response: self.__store_traffic(("<<", response.status, response.url)))

    def get_network_request(self, url: str):
        return [i for i in self.__traffic if '>>' in i and url in i[2]]

    def get_network_response(self, url: str):
        return [i for i in self.__traffic if '<<' in i and url in i[2]]

    def __store_traffic(self, tuple_):
        self.__traffic.append(tuple_)
        return self.__traffic
