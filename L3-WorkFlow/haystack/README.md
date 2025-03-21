# Haystack

Haystack 是一个端到端的开源框架，专注于使用 Transformer 模型构建 NLP 应用。它特别适合问答系统和搜索应用的开发。

## 主要特点

### 1. 模块化设计
- Reader组件
- Retriever组件
- Generator组件
- Pipeline系统

### 2. 检索能力
- 密集检索
- 稀疏检索
- 混合检索
- 跨语言检索

### 3. 集成支持
- 多种文档格式
- 主流数据库
- 开源模型
- 云服务API

## 快速开始

### 安装
```bash
pip install farm-haystack

# 可选依赖
pip install farm-haystack[colab,inference]
```

### 基础示例
```python
from haystack.nodes import PreProcessor, BM25Retriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from haystack.document_stores import ElasticsearchDocumentStore

# 初始化文档存储
document_store = ElasticsearchDocumentStore()

# 创建检索器和阅读器
retriever = BM25Retriever(document_store)
reader = FARMReader("deepset/roberta-base-squad2")

# 构建pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

# 查询
prediction = pipe.run(
    query="什么是Haystack框架？",
    params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)
```

## 核心组件

### 1. DocumentStore
- Elasticsearch
- FAISS
- Milvus
- PostgreSQL

### 2. Retriever
- 稠密检索
- BM25检索
- 表格检索
- 混合检索

### 3. Reader/Generator
- 问答模型
- 生成模型
- 摘要模型
- 翻译模型

## 应用场景

### 1. 智能问答
```python
from haystack.pipelines import GenerativeQAPipeline
from haystack.nodes import RAGenerator

# 创建生成式问答
generator = RAGenerator()
pipe = GenerativeQAPipeline(generator)

# 查询
response = pipe.run(
    query="如何使用Haystack构建问答系统？",
    documents=docs
)
```

### 2. 文档搜索
```python
from haystack.nodes import EmbeddingRetriever

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1"
)

# 语义搜索
results = retriever.retrieve(
    query="机器学习基础概念",
    top_k=5
)
```

## 最佳实践

### 1. 性能优化
- 批量处理
- 模型量化
- 缓存策略
- 并行计算

### 2. 准确性提升
- 模型选择
- 参数调优
- 数据预处理
- 后处理优化

### 3. 部署维护
- 监控指标
- 错误处理
- 版本管理
- 扩展性设计

## 系统架构

### 1. 核心模块
- 文档处理
- 向量检索
- 模型推理
- 结果整合

### 2. 外部依赖
- Elasticsearch
- FAISS
- Transformer
- PyTorch

### 3. 扩展接口
- REST API
- gRPC
- WebSocket
- 自定义接口

## 版本历史

- **1.0.0**: 基础功能发布
- **1.5.0**: 添加生成式模型
- **2.0.0**: 架构重构
- **2.2.0**: 性能优化

## 社区资源

- [官方文档](https://haystack.deepset.ai/)
- [GitHub仓库](https://github.com/deepset-ai/haystack)
- [示例集合](https://github.com/deepset-ai/haystack-tutorials)
- [社区论坛](https://github.com/deepset-ai/haystack/discussions)

## 常见问题

### 1. 资源需求
- GPU支持
- 内存优化
- 存储规划
- 并发处理

### 2. 集成问题
- 环境配置
- 依赖管理
- API兼容
- 数据迁移

## 贡献指南

1. 克隆项目
2. 安装依赖
3. 运行测试
4. 提交PR

## 许可证

Apache 2.0 