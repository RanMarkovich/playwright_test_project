class BrowserFactory:

    def __init__(self, p, env):
        self.p = p
        self.env = env
        self.configurations = {}

    def get_browser(self, type_: str = 'chrome'):
        return self.__browser_init(type_)

    def __browser_init(self, type_: str):
        browser, context = None, None
        if self.env == 'local':
            self.configurations['headless'] = False
        elif self.env == 'ci':
            self.configurations['headless'] = True
            self.configurations['args'] = ["--start-maximized"]
            if type_ == 'chrome':
                browser = self.p.chromium
            elif type_ == 'firefox':
                browser = self.p.firefox
            browser = browser.launch(**self.configurations)
            context = browser.new_context(no_viewport=True)
        return context
