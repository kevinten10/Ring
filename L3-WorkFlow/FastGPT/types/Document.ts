/**
 * 文档类型定义
 */
export interface Document {
  id: string;
  title: string;
  content: string;
  metadata: DocumentMetadata;
  vector?: number[];
}

/**
 * 文档元数据
 */
export interface DocumentMetadata {
  source: string;
  author?: string;
  createdAt: Date;
  updatedAt: Date;
  fileType: string;
  tags?: string[];
}

/**
 * 文档分块配置
 */
export interface ChunkConfig {
  chunkSize: number;
  chunkOverlap: number;
  separator?: string;
} 