import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

if __name__ == '__main__':
    llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V2.5",
                     api_key="sk-xxx",
                     base_url="https://api.siliconflow.cn")


    async def main():
        agent = Agent(
            task="打开链接 http，"
                 "分析xxx",
            llm=llm,
            use_vision=False,
        )
        result = await agent.run()
        print(result)


    asyncio.run(main())
