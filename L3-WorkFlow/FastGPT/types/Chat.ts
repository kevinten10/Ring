/**
 * 消息角色类型
 */
export type MessageRole = 'system' | 'user' | 'assistant';

/**
 * 消息类型定义
 */
export interface Message {
  role: MessageRole;
  content: string;
  timestamp: Date;
}

/**
 * 对话历史记录类型
 */
export interface ChatHistory {
  messages: Message[];
  metadata: ChatMetadata;
}

/**
 * 对话元数据类型
 */
export interface ChatMetadata {
  startTime: Date;
  endTime?: Date;
  knowledgeBaseId: string;
  tags?: string[];
}

/**
 * LLM 配置类型
 */
export interface LLMConfig {
  model: string;
  temperature: number;
  maxTokens: number;
  topP?: number;
  frequencyPenalty?: number;
  presencePenalty?: number;
} 