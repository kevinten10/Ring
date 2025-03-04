## 创建MCP python工具步骤

### 安装环境

1. 安装uv

uv主要是搭建mcp python sdk框架，并且mcp server通过uv指令启动mcp脚本

```bash
#windows环境
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

#liunx
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 安装pip

python环境必备

3. 使用uv初始化框架

不建议直接用cursor去写mcp逻辑，可能框架搭建上不对，会导致运行失败。
先通过标准的uv工具初始化框架，之后再让cursor去对应文件下写代码。

```bash
# Create a new directory for our project
uv init weather
cd weather

# Create virtual environment and activate it
uv venv

-------------------------
# 后面这些不用执行也行
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch weather.py
```

4. 使用cursor修改框架内容，生成对应的内容

这里建议用NOTEPADS功能，把需求描述清楚，然后可使用以下prompt生成代码：

```txt
@xxx 请根据该功能，实现MCP python程序，需要参考 @已有的mcp 目录下的代码进行实现。
将生成的代码放到 yyy 目录下的server.py中，并且生成对应的requirements.txt 文件。
```

建议让cursor参考已有的开源mcp脚本，这样生成的代码比较符合规范。

5. pip安装依赖

安装脚本所需要的依赖，切换到脚本目录下执行：

```bash
pip install -r requirements.txt
# 安装过可以不执行
pip install uv
```

6. 使用终端测试命令行

直接去cursor绑定mcp server，如果有问题会闪退，不会有报错信息。
这里可以先尝试用cmd之类的终端，运行一下，如果有报错会有error信息。
如果执行后没有报错，一般没有问题。

命令方式可参考参考文档：
Windows下注意路径，不行3种都试试

```bash
uv run --with fastmcp fastmcp run D:\Projects\ai\Ring\Python\appdependency\server.py
```

7. 配置cursor

配置到cursor的mcp server中，绿色为成功配置。

### 使用

1. 推荐在NOTEPADS中描述执行链路，这里给一个参考：

```markdown
现在，我需要你执行一个分析应用调用链路的任务，你可以使用 appinvoke 这个MCP工具。

### 执行链路

1. 我会给你1个原始的appid，你需要获取它依赖的服务，记录好相关数据
2. 根据它依赖的服务，你需要进行进一步搜索，分析它们所依赖的链路
3. 你需要记忆已经获取过的服务，如果1个服务依赖了已经扫描过的服务，你应该基于之前的数据，而不是重新获取它的数据，这可能会导致循环依赖

### 文档要求

工作目录：Python/appinvoke/analysis1 

1. 在每次分析完一个appid时，你应该在工作目录下，创建这个appid的分析报告
2. 在每次分析调用链路时，你应该在 route 文档中，更新依赖关系
3. 在全部分析完成后，你应该产出完整的调用关系说明和图示

### 其他要求

1. 依赖层级最多扫描10层，避免过深
2. 有些公共服务，无需进一步分析，例如
    1. log
    2. db
    3. search
```

2. 可以开启Agent模式的YOLO模式，自动执行MCP脚本

3. 告诉agent，执行上述脚本，并且给出初始参数

4. 开始执行，观察即可

5. 分析结果

### 辅助工具

1. [流程图渲染](https://mermaid-js.github.io/mermaid-live-editor)

2. [脑图绘制](https://app.napkin.ai)

## 参考文档

https://aibook.ren/archives/mcp-server-for-cursor