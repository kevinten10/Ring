import { Document } from './types/Document';
import { VectorStore } from './VectorStore';
import { DocumentProcessor } from './DocumentProcessor';

/**
 * 知识库管理类
 * 负责知识库的创建、文档处理、向量存储等功能
 */
export class KnowledgeBase {
  private id: string;
  private name: string;
  private description: string;
  private vectorStore: VectorStore;
  private documentProcessor: DocumentProcessor;

  constructor(id: string, name: string, description: string) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.vectorStore = new VectorStore();
    this.documentProcessor = new DocumentProcessor();
  }

  /**
   * 添加文档到知识库
   * @param document 文档对象
   */
  async addDocument(document: Document): Promise<boolean> {
    try {
      // 1. 处理文档
      const chunks = await this.documentProcessor.process(document);
      
      // 2. 向量化并存储
      await this.vectorStore.addDocuments(chunks);
      
      return true;
    } catch (error) {
      console.error('Failed to add document:', error);
      return false;
    }
  }

  /**
   * 搜索相关文档
   * @param query 查询文本
   * @param topK 返回结果数量
   */
  async search(query: string, topK: number = 5): Promise<Document[]> {
    try {
      const results = await this.vectorStore.search(query, topK);
      return results;
    } catch (error) {
      console.error('Failed to search documents:', error);
      return [];
    }
  }

  /**
   * 删除知识库中的文档
   * @param documentId 文档ID
   */
  async removeDocument(documentId: string): Promise<boolean> {
    try {
      await this.vectorStore.removeDocument(documentId);
      return true;
    } catch (error) {
      console.error('Failed to remove document:', error);
      return false;
    }
  }

  // Getters
  getId(): string {
    return this.id;
  }

  getName(): string {
    return this.name;
  }

  getDescription(): string {
    return this.description;
  }
} 