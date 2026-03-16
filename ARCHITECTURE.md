# System Architecture

## Overview

The application is a Flask API deployed on AWS EC2.

Observability components include:

- CloudWatch Logs
- CloudWatch Metrics
- CloudWatch Dashboard
- CloudWatch Alarms
- SNS Notifications

## Architecture Diagram

Client → Flask API → CloudWatch Logs  
Client → Flask API → CloudWatch Metrics  

Logs + Metrics → Dashboard  
Dashboard → Alarms → SNS Email

## Components

EC2  
Runs the Flask application

CloudWatch Logs  
Stores application logs

CloudWatch Metrics  
Stores custom metrics

CloudWatch Dashboard  
Visualizes system health

CloudWatch Alarms  
Detect abnormal behavior

SNS  
Sends alert notifications

## Technology Choices

Flask → lightweight API framework  
AWS EC2 → application hosting  
CloudWatch → monitoring and logging  
SNS → alert notifications
