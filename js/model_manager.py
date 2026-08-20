from enum import Enum
import os
class ModelType(Enum):
    DEEPSEEK="deepseek"; QWEN_ONLINE="qwen_online"; QWEN_OFFLINE="qwen_offline"
class ModelManager:
    def __init__(self):
        self.active=ModelType.QWEN_OFFLINE
        self.deepseek_key=os.getenv("DEEPSEEK_API_KEY","")
        self.dashscope_key=os.getenv("DASHSCOPE_API_KEY","")
    def switch(self,t:ModelType):
        if t==ModelType.DEEPSEEK and not self.deepseek_key: raise ValueError("DeepSeek Key ناقص")
        if t==ModelType.QWEN_ONLINE and not self.dashscope_key: raise ValueError("DashScope Key ناقص")
        self.active=t; return True
