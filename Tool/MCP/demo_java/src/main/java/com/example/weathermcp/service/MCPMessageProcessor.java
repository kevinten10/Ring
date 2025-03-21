package com.example.weathermcp.service;

import io.modelcontextprotocol.mcp.Message;
import io.modelcontextprotocol.mcp.MCPException;
import org.springframework.stereotype.Component;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;

@Component
public class MCPMessageProcessor {
    
    public String extractLocation(Message message) throws MCPException {
        try {
            // 从消息内容中提取location
            // 可以是JSON格式: {"location": "Beijing"}
            // 或者直接是文本格式: "Beijing"
            String content = message.getContent();
            
            if (content.startsWith("{")) {
                // JSON格式处理
                ObjectMapper mapper = new ObjectMapper();
                JsonNode node = mapper.readTree(content);
                return node.get("location").asText();
            } else {
                // 纯文本格式处理
                return content.trim();
            }
        } catch (Exception e) {
            throw new MCPException("Invalid location format: " + e.getMessage());
        }
    }
    
    public boolean validateLocation(String location) {
        // 验证location是否符合规则定义的格式
        return location != null && 
               location.matches("^[\\w\\s,]+$") && 
               location.length() > 0;
    }
} 