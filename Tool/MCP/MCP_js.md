# MCP JS 工具使用指南

## 1. 简介

MCP (Model-Controller-Pipeline) 是 Cursor IDE 中的一个强大工具，专门用于构建和运行 JavaScript 服务。本指南将帮助你从零开始掌握 MCP 工具的使用。

## 2. 环境配置

### 2.1 前置要求

在 Windows 系统上，你需要安装以下工具：

1. **Node.js**
   - 使用官方 MSI 安装包安装
   - 安装完成后会自动包含 npm

2. **pnpm** (可选)
   ```powershell
   Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
   ```

3. **查看 Node.js 全局安装路径**
   ```bash
   npm list --global
   ```
   > 记录此路径，后续配置需要用到

### 2.2 安装 MCP 服务

```bash
npm install -g @xxxx/xxx-mcp-server
```

### 2.3 Cursor 配置

在 Cursor 中配置 MCP 工具，需要使用绝对路径：

```json
{
    "playwright": {
        "command": "D:\\Users\\xxx\\Nodejs\\node.exe",
        "args": [
            "D:\\Users\\xxx\\AppData\\Roaming\\npm\\node_modules\\@executeautomation\\playwright-mcp-server\\dist\\index.js",
            "-y",
            "@smithery/cli@latest",
            "run",
            "@executeautomation/playwright-mcp-server",
            "--config",
            "\"{}\""
        ]
    }
}
```

> 注意：请将路径替换为你的实际安装路径

## 3. 项目开发流程

### 3.1 项目初始化
1. 克隆项目代码
2. 安装依赖：
   ```bash
   npm install
   ```

### 3.2 本地测试
在部署到 Cursor 前，建议在本地测试：
```bash
# 构建项目
npm run build

# 启动服务
npm start
```

### 3.3 调试技巧
1. 使用命令行直接启动服务进行调试
2. 通过 Cursor 的 MCP 日志查看详细错误信息
3. 使用以下命令验证服务：
   ```bash
   node {项目路径}/dist/index.js
   ```

## 4. 最佳实践

### 4.1 文档管理
- 维护清晰的 README 文档
- 记录 API 接口文档
- 保持更新变更日志
- 使用 Markdown 记录执行流程

### 4.2 执行流程示例

```markdown
# 应用调用链路分析任务

## 执行步骤
1. 输入初始 appid，获取依赖服务
2. 分析依赖服务的下级依赖
3. 记录已扫描服务，避免重复分析

## 文档规范
工作目录：Python/appinvoke/analysis1
- 为每个 appid 创建分析报告
- 在 route 文档中更新依赖关系
- 生成完整调用关系图示

## 注意事项
- 依赖扫描最多 10 层
- 跳过公共服务分析（如：log、db、search）
```

### 4.3 可视化工具推荐
1. [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor)
   - 用途：生成流程图
   - 特点：支持多种图表类型

2. [Napkin](https://app.napkin.ai)
   - 用途：制作思维导图
   - 特点：界面直观，易于使用

## 5. 故障排查

### 5.1 常见问题
1. **启动失败**
   - 检查依赖是否完整安装
   - 验证配置文件中的路径
   - 查看错误日志

2. **性能问题**
   - 控制依赖层级（≤10层）
   - 避免循环依赖
   - 合理使用缓存

### 5.2 优化建议
- 定期更新依赖包
- 使用 TypeScript 提高代码质量
- 实现自动化测试

## 6. 参考资源

- [MCP Server for Cursor 官方文档](https://aibook.ren/archives/mcp-server-for-cursor)
- [Windows 使用教程](https://medium.com/@sayharer/vscode-cline%E6%8F%92%E4%BB%B6%E9%83%A8%E7%BD%B2mcp-server-win%E7%B3%BB%E7%BB%9F-b079c3d254dc)
- [GitHub Issues](https://github.com/cline/cline/issues/1948)

## 7. 更新日志

### v1.0.0 (2024-03-21)
- 初始版本发布
- 完善环境配置说明
- 添加最佳实践指南
