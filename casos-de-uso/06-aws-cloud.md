# Caso de Uso 6: OpenCode + AWS/Cloud

## Descripción
Configurar infraestructura AWS, lambdas, y servicios cloud usando OpenCode como asistente de DevOps.

## Escenario
Un equipo necesita desplegar aplicaciones en AWS pero no tiene expertise en cloud.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Lambda function:**
```
@opencode Create an AWS Lambda function:
- API Gateway trigger
- DynamoDB integration
- Environment variables
- IAM role with minimal permissions
- Error handling
- CloudWatch logging
```

**Infraestructura como código:**
```
@opencode Create Terraform config for:
- VPC with public/private subnets
- ECS cluster with Fargate
- RDS PostgreSQL
- ElastiCache Redis
- S3 bucket for static assets
```

**Configurar CI/CD para AWS:**
```
@opencode Create GitHub Actions workflow for:
- Build and push to ECR
- Deploy to ECS with zero downtime
- Run tests before deployment
- Rollback on failure
```

### 2. Flujo de Trabajo
1. Describe la arquitectura que necesitas
2. OpenCode genera la configuración
3. Incluye permisos IAM mínimos
4. Agrega monitoreo y logging
5. Documenta costos estimados

## Beneficios
- Configuración más rápida
- Mejores prácticas de seguridad
- Costos optimizados
- Infraestructura como código

## Archivos del Caso
- `06-aws/lambda_function.py`
- `06-aws/terraform/main.tf`
- `06-aws/deploy.yml`
