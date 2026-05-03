import json
from mimimo_llm import MimimoLLM

class EnergyAnalyzer:
    def __init__(self, data_path="data/mock_devices.json"):
        self.data_path = data_path
        self.llm = MimimoLLM()

    def load_data(self):
        """加载设备数据"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("❌ 错误：未找到设备数据文件")
            return []

    def run(self):
        """主运行循环"""
        devices = self.load_data()
        if not devices:
            return

        print(f"\n🔋 系统启动：正在监控 {len(devices)} 台设备...\n")

        # 模拟用户输入
        user_input = "昨天家里哪个设备最费电？有什么省电建议？"
        print(f"🗣️ 用户提问: {user_input}")

        # 调用 Mimimo AI 进行分析
        result = self.llm.analyze_prompt(user_input, devices)
        
        print(result)

if __name__ == "__main__":
    analyzer = EnergyAnalyzer()
    analyzer.run()