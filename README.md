### 1. Overview
This API enables businesses to enhance their website search functionality using embeddings-based search. The API allows clients to:
- Submit product data for storage and embedding conversion.
- Perform intelligent search queries using natural language.
- Sync product updates in real time using webhooks.
### 2. Authentication
All endpoints require an API Key or JWT token for secure access. Clients must include an authentication header:
```Authorization: Bearer YOUR_API_KEY

```
### 3. Endpoints
#### 3.1 Product Submission (Store & Embed)
Endpoint: POST /products
Description: Clients submit product data, which is stored and converted into vector embeddings.
Request Body:
```{
  "id": "12345",
  "name": "Wireless Headphones",
  "description": "Noise-canceling Bluetooth headphones",
  "category": "Electronics",
  "price": 99.99
}

```
Response:
```{
  "status": "success",
  "message": "Product added successfully"
}

```
#### 3.2 Search API (Query by Meaning)
Endpoint: GET /search?query=...
Description: Search for products using embeddings instead of keywords.
Response Example:
```{
  "results": [
    {
      "id": "12345",
      "name": "Wireless Headphones",
      "score": 0.87
    }
  ]
}

```
#### 3.3 Webhook-Based Sync API
Endpoint: POST /sync
Description: Clients notify the API when a product is added, updated, or deleted.
Request Body:
```{
  "event": "update",
  "product": {
    "id": "12345",
    "name": "Wireless Headphones",
    "description": "Updated description",
    "category": "Electronics",
    "price": 99.99
  },
  "timestamp": 1709640000,
  "signature": "a1b2c3d4e5f6..."
}

```
Response:
```{
  "status": "success",
  "message": "Product sync processed"
}

```
### 4. Security Measures
- API Key Authentication: Ensures only authorized clients can access endpoints.
- Webhook Signature Verification: Uses HMAC to verify authenticity of webhook requests.
- Rate Limiting: Prevents abuse by limiting API calls per client.
- Retry Mechanism: Webhooks support retries with exponential backoff for reliability.
### 5. Deployment & Scalability
- Cloud-Based Hosting: API is deployed in a scalable cloud environment.
- FAISS Index Optimization: Ensures high-speed vector search operations.
- Asynchronous Processing: For batch processing and high-volume requests.
### 6. Conclusion
This API transforms traditional search into an AI-driven experience, providing businesses with more relevant search results and seamless real-time updates. By leveraging FAISS and all-MiniLM-L6-v2, we ensure superior search performance that scales with client needs.
🚀 Ready to integrate? Contact us for API access and onboarding support!
