import { KnowledgeBase } from './KnowledgeBase';
import { Message, ChatHistory } from './types/Chat';
import { LLMService } from './LLMService';

/**
 * 对话管理类
 * 负责处理用户对话、上下文管理、模型调用等功能
 */
export class ChatManager {
  private knowledgeBase: KnowledgeBase;
  private llmService: LLMService;
  private history: ChatHistory;

  constructor(knowledgeBase: KnowledgeBase) {
    this.knowledgeBase = knowledgeBase;
    this.llmService = new LLMService();
    this.history = {
      messages: [],
      metadata: {
        startTime: new Date(),
        knowledgeBaseId: knowledgeBase.getId()
      }
    };
  }

  /**
   * 发送消息并获取回复
   * @param message 用户消息
   */
  async sendMessage(message: string): Promise<Message> {
    try {
      // 1. 保存用户消息
      const userMessage: Message = {
        role: 'user',
        content: message,
        timestamp: new Date()
      };
      this.history.messages.push(userMessage);

      // 2. 搜索相关文档
      const relevantDocs = await this.knowledgeBase.search(message);

      // 3. 构建系统提示词
      const systemPrompt = this.buildSystemPrompt(relevantDocs);

      // 4. 调用 LLM 获取回复
      const response = await this.llmService.complete({
        messages: [
          { role: 'system', content: systemPrompt },
          ...this.history.messages
        ]
      });

      // 5. 保存助手回复
      const assistantMessage: Message = {
        role: 'assistant',
        content: response,
        timestamp: new Date()
      };
      this.history.messages.push(assistantMessage);

      return assistantMessage;
    } catch (error) {
      console.error('Failed to process message:', error);
      throw error;
    }
  }

  /**
   * 获取对话历史
   */
  getHistory(): ChatHistory {
    return this.history;
  }

  /**
   * 清空对话历史
   */
  clearHistory(): void {
    this.history.messages = [];
  }

  /**
   * 导出对话历史
   */
  exportHistory(): string {
    return JSON.stringify(this.history, null, 2);
  }

  private buildSystemPrompt(relevantDocs: any[]): string {
    const context = relevantDocs
      .map(doc => doc.content)
      .join('\n\n');
    
    return `你是一个知识库助手。请基于以下参考资料回答用户问题：\n\n${context}`;
  }
} 