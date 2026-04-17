📂 SaaS Stack
┃
┣ 📂 Frontend
┃ ┣ 📂 React
┃ ┣ 📂 NextJS
┃ ┣ 📂 Vue
┃ ┣ 📂 TailwindCSS
┃ ┗ 📂 Shadcn UI
┃
┣ 📂 Backend
┃ ┣ 📂 NodeJS
┃ ┣ 📂 Django
┃ ┣ 📂 Laravel
┃ ┣ 📂 FastAPI
┃ ┗ 📂 Express
┃
┣ 📂 Database
┃ ┣ 📂 PostgreSQL
┃ ┣ 📂 MySQL
┃ ┣ 📂 MongoDB
┃ ┣ 📂 Redis
┃ ┗ 📂 Supabase
┃
┣ 📂 Auth
┃ ┣ 📂 Clerk
┃ ┣ 📂 Auth0
┃ ┣ 📂 Firebase Auth
┃ ┣ 📂 Supabase Auth
┃ ┗ 📂 NextAuth
┃
┣ 📂 Payments
┃ ┣ 📂 Stripe
┃ ┣ 📂 Paddle
┃ ┣ 📂 Dodo Payments
┃ ┣ 📂 Lemon Squeezy
┃ ┗ 📂 Polar
┃
┣ 📂 Emails
┃ ┣ 📂 Resend
┃ ┣ 📂 SendGrid
┃ ┣ 📂 Mailgun
┃ ┣ 📂 Postmark
┃ ┗ 📂 Amazon SES
┃
┣ 📂 Storage
┃ ┣ 📂 AWS
┃ ┣ 📂 Cloudflare 
┃ ┣ 📂 Google Cloud Storage
┃ ┣ 📂 Supabase Storage
┃ ┗ 📂 Uploadcare
┃
┣ 📂 Deployment
┃ ┣ 📂 Vercel
┃ ┣ 📂 Netlify
┃ ┣ 📂 Railway
┃ ┣ 📂 Render
┃ ┗ 📂 AWS
┃
┣ 📂 Domains and DNS
┃ ┣ 📂 Namecheap
┃ ┣ 📂 Hostinger
┃ ┣ 📂 Cloudflare DNS
┃ ┣ 📂 Google Domains
┃ ┗ 📂 SiteGround
┃
┣ 📂 Analytics
┃ ┣ 📂 Google Analytics
┃ ┣ 📂 Plausible
┃ ┣ 📂 PostHog
┃ ┣ 📂 Mixpanel
┃ ┗ 📂 DataFast
┃
┣ 📂 Monitoring
┃ ┣ 📂 Sentry
┃ ┣ 📂 LogRocket
┃ ┣ 📂 Datadog
┃ ┣ 📂 NewRelic
┃ ┗ 📂 UptimeRobot
┃
┣ 📂 DevOps
┃ ┣ 📂 Docker
┃ ┣ 📂 Kubernetes
┃ ┣ 📂 GitHub Actions
┃ ┣ 📂 CI CD
┃ ┗ 📂 Terraform
┃
┣ 📂 Search
┃ ┣ 📂 Algolia
┃ ┣ 📂 Meilisearch
┃ ┣ 📂 Elasticsearch
┃ ┣ 📂 Typesense
┃ ┗ 📂 OpenSearch
┃
┣ 📂 AI Integration
┃ ┣ 📂 OpenAI API
┃ ┣ 📂 Anthropic API
┃ ┣ 📂 Replicate
┃ ┣ 📂 HuggingFace
┃ ┗ 📂 Gemini API
┃
┣ 📂 Integrations
┃ ┣ 📂 Zapier
┃ ┣ 📂 Make
┃ ┣ 📂 n8n
┃ ┣ 📂 Pabbly
┃ ┗ 📂 Webhooks
┃
┣ 📂 Security
┃ ┣ 📂 SSL
┃ ┣ 📂 Cloudflare
┃ ┣ 📂 WAF
┃ ┣ 📂 Rate Limiting
┃ ┗ 📂 Secrets Management
┃
┣ 📂 Marketing
┃ ┣ 📂 Search Console
┃ ┣ 📂 Outrank
┃ ┣ 📂 Buffer
┃ ┣ 📂 Analytics
┃ ┗ 📂 Kit
┃
┗ 📂 Customer Support
  ┣ 📂 Intercom
  ┣ 📂 Crisp
  ┣ 📂 Zendesk
  ┣ 📂 Tawk
  ┗ 📂 HelpScout
  
  
  System Design Detailed Roadmap
|
| | |-- Fundamentals
| |-- What is System Design
| | |-- High level vs low level design
| | |-- Functional vs non-functional requirements
| | |-- Scalability, availability, reliability
| |-- Core Concepts
| | |-- Latency vs throughput
| | |-- Consistency vs availability (CAP theorem)
| | |-- Horizontal vs vertical scaling
| |-- Architecture Basics
| | |-- Monolith vs microservices
| | |-- Client-server architecture
| | |-- Load balancing basics

| | |-- Core Components
| |-- Web Servers
| | |-- Nginx, Apache
| |-- Application Servers
| | |-- Business logic layer
| |-- Databases
| | |-- SQL vs NoSQL
| |-- Caching
| | |-- Redis, Memcached
| |-- Load Balancers
| | |-- Round robin, least connections

| | |-- Data Management
| |-- Database Design
| | |-- Schema design
| | |-- Indexing
| |-- Replication
| | |-- Master-slave
| | |-- Multi-master
| |-- Partitioning
| | |-- Sharding
| | |-- Horizontal partitioning
| |-- Data Consistency
| | |-- Strong vs eventual consistency

| | |-- Scalability & Performance
| |-- Caching Strategies
| | |-- Cache aside
| | |-- Write through / write back
| |-- CDN
| | |-- Edge caching
| |-- Asynchronous Processing
| | |-- Message queues
| | |-- Event-driven systems
| |-- Rate Limiting
| | |-- Token bucket
| | |-- Leaky bucket

| | |-- System Design Patterns
| |-- API Gateway
| |-- Circuit Breaker
| |-- Retry Mechanism
| |-- Bulkhead Pattern
| |-- Saga Pattern
| |-- CQRS
| |-- Event Sourcing

| | |-- Distributed Systems
| |-- Distributed Coordination
| | |-- Zookeeper basics
| |-- Consensus Algorithms
| | |-- Paxos
| | |-- Raft
| |-- Distributed Transactions
| | |-- Two-phase commit
| |-- Service Discovery

| | |-- Security & Reliability
| |-- Authentication & Authorization
| | |-- OAuth, JWT
| |-- Data Security
| | |-- Encryption at rest & in transit
| |-- Fault Tolerance
| | |-- Redundancy
| | |-- Failover systems
| |-- Monitoring & Logging
| | |-- Metrics, tracing, alerting

| | |-- DevOps & Infrastructure
| |-- CI/CD Pipelines
| |-- Containerization
| | |-- Docker
| |-- Orchestration
| | |-- Kubernetes
| |-- Cloud Platforms
| | |-- AWS
| | |-- GCP
| | |-- Azure
| |-- Infrastructure as Code
| | |-- Terraform

| | |-- Real World System Design
| |-- Design URL Shortener
| |-- Design Chat System
| |-- Design Social Media Feed
| |-- Design Video Streaming Platform
| |-- Design E-commerce System
| |-- Design Ride Sharing App

| | |-- Performance Optimization
| |-- Bottleneck Identification
| |-- Horizontal scaling strategies
| |-- Database query optimization
| |-- Efficient resource utilization

| | |-- Interview Preparation
| |-- System design interview framework
| |-- Requirement clarification
| |-- Component breakdown
| |-- Trade-off discussions
| |-- Whiteboard communication

| | |-- Projects
| |-- Build scalable REST API
| |-- Implement caching layer with Redis
| |-- Design distributed logging system
| |-- Build real-time notification system
| |-- Create load balanced microservices app
| |-- Design event-driven architecture

| | |-- Community and Growth
| |-- Read system design case studies
| |-- Contribute to open source
| |-- Write technical blogs
| |-- Share designs on LinkedIn
| |-- Practice daily system design

Grab this ebook to Master System Design
https://codewithdhanian.gumroad.com/l/urcjee

![[Pasted image 20260412211409.png]]


![[Pasted image 20260412211753.png]]
![[c758184c57e860aaaa6037d25633dddc.png]]

![[4f05f1e4771dd51d5a328c410b778bcf.png]]