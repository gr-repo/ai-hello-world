import os, platform

class MySettings:
    
    def __call__(self, *args, **kwds):
        self.OPENAI_API_KEY = 'YOURKEY'
        
    def get(self):
        
        if self.is_codespaces():
            print("Getting keys from environment variables")
            self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            
            return self
        
        print('Setup your keys')
        
    def is_codespaces(self):
        return (
            os.getenv("CODESPACES") == "true"
            or os.getenv("CODESPACE_NAME") is not None
            or "codespaces" in platform.node().lower()
        )