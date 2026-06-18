# Learning the FastAPI Backend Engineering 
### At the end we will be creating the application with the following endpoints or tables

- Users
- Organizations
- Projects
- Tasks
- Comments
- Attachments
- Notifications
- JWT Authentication
- RBAC
- Redis
- Celery
- RabbitMQ
- Kafka
- Monitoring
- Logging
- Metrics
- Docker
- Kubernetes
- Microservices
- Production Deployment

### Final Architecture We Are Working Toward
                    Users
                      │
                      ▼

                Load Balancer
                      │
                      ▼

              FastAPI Application
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼

 PostgreSQL         Redis         RabbitMQ
(Database)        (Cache)        (Queues)

                                      │
                                      ▼

                                Celery Workers

                                      │
                                      ▼

                             Email Service

                                      │
                                      ▼

                                   Kafka

                                      │
                                      ▼

                            Analytics Service




