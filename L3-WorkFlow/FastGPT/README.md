# FastGPT 模块

FastGPT 模块是一个强大的知识库问答系统，支持文档管理、智能对话和多模型接入。本模块帮助用户快速构建自己的知识库问答应用。

## 核心功能

### 1. 知识库管理 (KnowledgeBase)
- 文档导入与处理
- 自动文本分段
- 向量化存储
- 语义检索

### 2. 对话管理 (ChatManager)
- 多轮对话支持
- 上下文管理
- 对话历史记录
- 对话导出功能

### 3. 文档处理 (DocumentProcessor)
- 支持多种文件格式
  - PDF
  - Word
  - Markdown
  - 纯文本
- 智能分段算法
- 文档向量化

## 系统架构

```
FastGPT/
├── types/              # 类型定义
│   ├── Document.ts     # 文档相关类型
│   └── Chat.ts         # 对话相关类型
├── KnowledgeBase.ts    # 知识库管理类
├── ChatManager.ts      # 对话管理类
├── DocumentProcessor.ts # 文档处理类
├── VectorStore.ts      # 向量存储类
└── LLMService.ts       # LLM服务类
```

## 使用方法

### 1. 初始化知识库

```typescript
import { KnowledgeBase } from './KnowledgeBase';

const kb = new KnowledgeBase(
  'kb-001',
  '技术文档库',
  '存储技术相关文档'
);
```

### 2. 添加文档

```typescript
const document = {
  id: 'doc-001',
  title: '入门指南',
  content: '这是一份入门指南...',
  metadata: {
    source: 'internal',
    author: 'admin',
    createdAt: new Date(),
    updatedAt: new Date(),
    fileType: 'markdown',
    tags: ['guide', 'tutorial']
  }
};

await kb.addDocument(document);
```

### 3. 创建对话

```typescript
import { ChatManager } from './ChatManager';

const chatManager = new ChatManager(kb);
const response = await chatManager.sendMessage('如何开始使用这个系统？');
```

## 配置说明

### 文档分块配置

```typescript
const chunkConfig = {
  chunkSize: 500,    // 每块文本的最大长度
  chunkOverlap: 50,  // 相邻块的重叠长度
  separator: '\n'    // 分隔符
};
```

### LLM 配置

```typescript
const llmConfig = {
  model: 'gpt-3.5-turbo',
  temperature: 0.7,
  maxTokens: 2000,
  topP: 0.95
};
```

## API 接口

### 知识库管理

```typescript
POST /api/knowledge/create
POST /api/knowledge/upload
GET  /api/knowledge/search
DELETE /api/knowledge/document
```

### 对话管理

```typescript
POST /api/chat/completion
GET  /api/chat/history
POST /api/chat/export
DELETE /api/chat/clear
```

## 最佳实践

1. **文档预处理**
   - 合理设置分块大小
   - 保持适当的块重叠度
   - 清理无关内容

2. **向量索引优化**
   - 定期更新向量索引
   - 设置合适的相似度阈值
   - 优化检索数量

3. **对话质量提升**
   - 优化系统提示词
   - 合理设置上下文长度
   - 定期清理历史记录

## 注意事项

1. 文档大小限制：单个文档建议不超过 10MB
2. 并发处理：建议使用队列处理大量文档
3. 向量存储：定期备份向量数据
4. 隐私保护：注意敏感信息处理

## 开发计划

- [ ] 支持更多文档格式
- [ ] 添加文档预处理管道
- [ ] 优化向量检索算法
- [ ] 增加多语言支持
- [ ] 添加用户权限管理 