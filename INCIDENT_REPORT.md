# Incident Report: Error Spike in Observable Service

## Overview

This incident simulation demonstrates how observability tools were used to detect and diagnose an application failure in the Observable Service.

The system is a Flask-based API deployed on an EC2 instance with structured logging, custom metrics, CloudWatch monitoring dashboards, and alerting.

---

## Incident Details

Incident Type: Error Spike  
Detection Method: CloudWatch Alarm  
Date: March 15, 2026  
Affected Endpoint: /error  

---

## Detection

The issue was detected automatically by a CloudWatch alarm named:

HighErrorRate

The alarm monitors the custom metric:

ErrorCount

Condition:

ErrorCount > 5 within 1 minute

When multiple requests were sent to the `/error` endpoint, the alarm transitioned from:

OK → ALARM

An email notification was sent through SNS.

**Screenshot:**  
(Insert alarm triggered screenshot)

---

## Impact

Users calling the `/error` endpoint received HTTP 500 responses.

Although this endpoint was intentionally created for simulation, similar failures in production could impact application reliability and user experience.

---

## Investigation

The investigation used observability tools:

### 1. CloudWatch Dashboard

The monitoring dashboard showed a spike in:

ErrorCount  
RequestCount

This confirmed abnormal behavior.

**Screenshot:**  
(Insert dashboard spike screenshot)

---

### 2. CloudWatch Logs

Logs revealed repeated requests to `/error` with status code 500.

Example log entry:

```json
{
 "event": "simulated_error",
 "path": "/error",
 "status_code": 500
}
