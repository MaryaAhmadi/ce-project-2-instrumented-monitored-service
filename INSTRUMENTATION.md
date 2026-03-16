# Instrumentation

## Logging Strategy

The application uses structured JSON logging with structlog.

Each request generates logs containing:

- correlation_id
- request path
- status code
- latency
- log level

Example log entry:

{
 "event": "request_completed",
 "path": "/error",
 "status_code": 500,
 "latency_ms": 10
}

## Correlation ID

Each request receives a unique correlation ID.

This allows tracing a request across logs and metrics.

## Custom Metrics

Metrics sent to CloudWatch:

RequestCount  
ErrorCount  
OrdersCreated  
OrderValue
Apilatency

## Why These Metrics Matter

RequestCount → traffic monitoring  
ErrorCount → reliability monitoring  
OrdersCreated → business activity  
OrderValue → revenue insight
ApiLatency → measures how long the API takes to respond to requests in milliseconds.
This metric is important for detecting slow endpoints and latency spikes.
