---
title: "Integration Scenarios"
order: 5
description: "Explore different integration scenarios including Frontend-Backend, AI-Backend, and Monolith-Microservice patterns."
---

# Integration Scenarios

## Frontend ←→ Backend

**Use Case**: Connect frontend applications to backend services without REST APIs.

**Steps:**

1. **Run the gateway with your backend**
   ```bash
   gcg.exe --projectKey [yourKey] --env DEV
   ```

2. **Generate your graft**
   ```bash
   npm install @graftcode/backend-service
   ```

3. **Call any method, anywhere**
   ```typescript
   import { BackendService } from '@graftcode/backend-service';
   
   const backend = new BackendService();
   const data = await backend.getUserData(userId);
   ```

## AI ←→ Backend

**Use Case**: Enable AI agents to interact with backend services seamlessly.

**Steps:**

1. **Run the gateway with your service**
   ```bash
   gcg.exe --projectKey [yourKey] --env DEV
   ```

2. **Generate your graft**
   ```bash
   npm install @graftcode/ai-service
   ```

3. **Call any method, anywhere**
   ```typescript
   import { AIService } from '@graftcode/ai-service';
   
   const aiService = new AIService();
   const result = await aiService.processRequest(request);
   // Choose & Change your PaaS channel, communication protocol 
   // or integration architecture with simple config change in production
   ```

## Monolith ←→ Microservice

**Use Case**: Achieve modular monolith experience with easy transition to microservices.

**Steps:**

1. **Run the gateway with your service**
   ```bash
   gcg.exe --projectKey [yourKey] --env DEV
   ```

2. **Generate your graft**
   ```bash
   npm install @graftcode/microservice
   ```

3. **Call any method, anywhere**
   ```typescript
   import { Microservice } from '@graftcode/microservice';
   
   const service = new Microservice();
   // Change invocation target through simple configuration change
   // Select in-memory and switch to remote in production with zero code-change
   ```
