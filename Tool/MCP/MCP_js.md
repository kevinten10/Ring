# MCP JS工具使用指南

## 1. 概述
MCP (Model-Controller-Pipeline) 是Cursor IDE中的一个强大工具，用于构建和运行JS服务。本指南将帮助你从零开始搭建和使用MCP工具。

## 2. 环境准备

### 2.1 必要工具安装
1. npm工具安装

2. pnpm安装

```bash
Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
```

2. nodejs工具安装

### 2.2 项目初始化 

## 3. 开发流程
 
### 3.1 拉取代码

克隆代码库

### 3.2 依赖管理
```bash
# 安装项目依赖
npm install 
```

## 4. 测试与部署

### 4.1 本地测试
在部署到Cursor之前，建议先在终端中测试：

```bash
npm run build

npm start
```

### 4.2 Cursor配置
1. 在Cursor中配置MCP server
2. 确认配置状态（绿色表示成功）

```bash
node {ABSOLUTE PATH TO FILE HERE}/dist/index.js
```

## 5. 最佳实践

### 5.1 项目文档管理
- 在Notepad中记录执行流程
- 创建清晰的README文档
- 记录API接口文档
- 维护变更日志

执行流程示例：
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

### 5.2 自动化执行
1. 使用Agent的YOLO模式实现自动执行
2. 设置合适的执行参数
3. 监控执行过程

### 5.3 结果分析与可视化
推荐工具：
1. [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor) - 流程图绘制
2. [Napkin](https://app.napkin.ai) - 思维导图制作

## 6. 常见问题处理
1. 启动失败排查
   - 检查依赖是否完整安装
   - 验证路径配置是否正确
   - 查看终端错误日志

2. 性能优化建议
   - 控制依赖层级（建议不超过10层）
   - 避免循环依赖
   - 合理使用缓存机制

## 7. 参考资源
- [MCP Server for Cursor 官方文档](https://aibook.ren/archives/mcp-server-for-cursor)
- 项目示例和模板
- 常见问题解答

## 8. 更新日志
记录文档的重要更新和变更... 