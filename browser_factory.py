class BrowserFactory:

    def __init__(self, p, env):
        self.p = p
        self.env = env

    def get_browser(self, type_: str = 'chrome'):
        return self.__browser_init(type_)

    def __browser_init(self, type_: str):
        browser, context = None, None
        launch_config, context_config = {}, {}
        if self.env == 'local':
            launch_config['headless'] = False
            context_config['no_viewport'] = True
        elif self.env == 'ci':
            launch_config['headless'] = True
            context_config['viewport'] = {'width': 1500, 'height': 700}
        if type_ == 'chrome':
            browser = self.p.chromium
        elif type_ == 'firefox':
            browser = self.p.firefox
        launch_config['args'] = ["--start-maximized"]
        browser = browser.launch(**launch_config)
        context = browser.new_context(**context_config)
        return context
