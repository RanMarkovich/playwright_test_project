class BrowserFactory:

    def __init__(self, p, env):
        self.p = p
        self.env = env
        self.launch_config = {}
        self.context_config = {}

    def get_browser(self, type_: str = 'chrome'):
        return self.__browser_init(type_)

    def __browser_init(self, type_: str):
        browser, context = None, None
        if self.env == 'local':
            self.launch_config['headless'] = True
            self.context_config['no_viewport'] = True
        elif self.env == 'ci':
            self.launch_config['headless'] = True
            self.context_config['viewport'] = {'width': 1500, 'height': 700}
        if type_ == 'chrome':
            browser = self.p.chromium
        elif type_ == 'firefox':
            browser = self.p.firefox
        self.launch_config['args'] = ["--start-maximized"]
        browser = browser.launch(**self.launch_config)
        context = browser.new_context(**self.context_config)
        return context
