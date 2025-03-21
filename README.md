# AI 导航与介绍

本项目收集和整理了当前主流的AI模型和工具信息，帮助你了解和选择合适的AI解决方案。

## 目录结构
```
│
├── LLM/             # 大语言模型目录
│   ├── chatgpt/     # OpenAI的ChatGPT
│   ├── claude/      # Anthropic的Claude
│   ├── gemini/      # Google的Gemini
│   ├── grok/        # xAI的Grok
│   ├── qianwen/     # 阿里云通义千问
│   ├── ernie/       # 百度文心一言
│   ├── doubao/      # 字节跳动豆包
│   ├── monica/      # 智谱AI Monica
│   ├── kimi/        # Moonshot AI Kimi
│   └── deepseek/    # DeepSeek
│
├── Application/            # AI工具目录
│   ├── cursor/      # AI编程工具
│   ├── coze/        # 对话机器人平台
│   ├── dify/        # AI应用开发平台
│   ├── codeium/     # AI代码助手
│   ├── copilot/     # GitHub AI助手
│   ├── midjourney/  # AI图像生成
│   ├── stable_diffusion/ # 开源图像生成
│   ├── notion_ai/   # Notion AI助手
│   ├── napkin_ai/   # AI手绘转设计工具
│   ├── ideogram_ai/ # AI文字艺术设计工具
│   └── gamma/       # AI演示文档工具
├── L3-WorkFlow/    # AI工作流框架目录
│   ├── langchain/  # LangChain框架
│   ├── fastgpt/    # FastGPT框架
│   ├── flowise/    # Flowise可视化工作流
│   └── haystack/   # Haystack NLP框架
└── README.md        # 本文件
```

## 项目特点

### 1. AI模型导航
- 全面收录主流AI模型
- 详细的功能对比
- 使用场景推荐
- 最新更新动态

### 2. AI工具集成
- 丰富的工具生态
- 场景化解决方案
- 实用性评测
- 使用教程

## 快速选择指南

### 1. 选择大语言模型 (LLM)

#### 国内用户推荐
- 日常对话：文心一言、通义千问、Kimi
- 学术研究：Monica、通义千问
- 编程开发：DeepSeek
- 多模态任务：Kimi、文心一言

#### 国际用户推荐
- 通用对话：ChatGPT、Claude
- 代码开发：ChatGPT、GitHub Copilot
- 学术研究：Claude
- 多模态任务：Gemini

### 2. 选择AI工具 (Application)

#### 开发工具
- 代码编辑器：Cursor
- 代码补全：GitHub Copilot、Codeium
- 知识库构建：FastGPT
- AI工作流：参考 L3-WorkFlow 目录

#### 创意工具
- 图像生成：Midjourney（商用）、Stable Diffusion（开源）
- 文档创作：Notion AI、Gamma
- 设计工具：Napkin AI（手绘转设计）、Ideogram AI（文字艺术）

## 使用建议

### 个人用户
1. **免费方案**
   - 基础对话：国内免费LLM
   - 代码开发：Codeium
   - 图像生成：Stable Diffusion
   - AI工作流：参考 L3-WorkFlow 目录下的开源方案
   - 文档创作：Gamma免费版
   - 设计创意：Napkin AI、Ideogram AI免费版

2. **付费方案**
   - 通用对话：ChatGPT Plus
   - 代码开发：GitHub Copilot
   - 图像生成：Midjourney
   - 知识库：FastGPT商业版
   - 文档协作：Notion AI
   - 专业设计：Gamma专业版

### 企业用户
1. **中小企业**
   - 混合使用免费和基础版服务
   - 使用LangChain构建自定义AI应用
   - 使用FastGPT搭建企业知识库
   - 按需选择专业版功能
   - 可自建知识库系统

2. **大型企业**
   - 选择企业版服务
   - 考虑私有化部署方案
   - 定制化知识库方案

## 注意事项
1. 数据安全
   - 注意敏感信息保护
   - 遵守数据合规要求
   - 定期数据备份

2. 成本控制
   - 合理使用免费额度
   - 优化API调用策略
   - 资源复用

3. 效果优化
   - 提示词优化
   - 多模型协同
   - 知识库维护

## 开发计划
1. 持续更新AI模型信息
2. 扩展工具生态系统
3. 优化知识库系统
4. 添加更多使用案例

## 贡献指南
欢迎贡献新的AI模型和工具信息，以及改进知识库系统。如发现问题或有建议，请提出issue。

## 许可证
本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

### 主要功能

- **知识库管理**
  - 支持多种格式文档导入（PDF、Word、Markdown等）
  - 文档自动分段和向量化
  - 知识库分类管理
  
- **对话管理**
  - 支持多轮对话
  - 对话历史记录
  - 对话导出功能

- **模型配置**
  - 支持多种 LLM 模型接入
  - 可配置提示词模板
  - 参数动态调整

## AI工作流框架概述

### 框架分类
1. **开发框架类**
   - 面向开发者的完整开发框架
   - 提供灵活的定制能力
   
2. **低代码平台类**
   - 可视化开发工具
   - 快速应用构建平台

3. **垂直应用类**
   - 特定场景的专业解决方案
   - 开箱即用的功能组件

### 详细信息
更多框架详情和对比分析，请参考 [L3-WorkFlow](./L3-WorkFlow/README.md) 目录。
