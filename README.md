# 🚀 Enterprise Cloud Platform: AWS + Kubernetes + GitOps

> **Status do Projeto:** Production-Ready Framework (Framework Pronto para Produção) 🛠️

Este repositório contém a implementação de uma plataforma de engenharia moderna, utilizando o conceito de **Internal Developer Platform (IDP)**. O foco é automatizar o provisionamento de infraestrutura em nuvem e a entrega de software com máxima segurança, observabilidade e controle de custos.

---

## 📄 Visão Geral e Contexto de Negócio

No cenário atual de transformação digital, muitas empresas enfrentam o **"Gargalo da Agilidade"**. A infraestrutura manual ou mal estruturada gera:
*   **Lentidão no Time-to-Market:** Demora de dias ou semanas para subir novos ambientes.
*   **Erros Humanos:** Configurações inconsistentes entre ambientes de Dev e Prod.
*   **Custos Incontroláveis:** Gastos excessivos em Cloud por falta de visibilidade e governança.

**Este projeto resolve essas dores através de:**
1.  **Infraestrutura como Código (IaC):** Replicação idêntica de ambientes em minutos.
2.  **GitOps:** O Git como a única fonte da verdade para o estado do cluster.
3.  **Observabilidade Nativa:** Monitoramento proativo para evitar downtime.

---

## 🏗️ Arquitetura da Solução

A solução foi desenhada seguindo as melhores práticas de arquitetura da AWS (Well-Architected Framework), focada em alta disponibilidade e isolamento de rede.

![Arquitetura da Solução](./docs/diagrams/full_architecture.png)

### Diferenciais Técnicos:
*   **Isolamento de Rede:** Clusters EKS operando em Subnets Privadas com saída via NAT Gateway.
*   **Código DRY (Don't Repeat Yourself):** Uso do **Terragrunt** para gerenciar múltiplos ambientes e contas AWS sem duplicidade de código.
*   **Bootstrap Automático:** Implementação do padrão *App-of-Apps* com **Argo CD**, permitindo que a plataforma se "auto-instale" a partir do repositório Git.

---

## 🛠️ Stack Tecnológica

| Camada | Ferramentas |
| :--- | :--- |
| **Cloud Provider** | Amazon Web Services (AWS) |
| **Infraestrutura (IaC)** | Terraform & Terragrunt |
| **Orquestração** | Kubernetes (Amazon EKS v1.29) |
| **Entrega Contínua (GitOps)** | Argo CD |
| **Gestão de Cluster** | Rancher Manager |
| **Observabilidade** | Prometheus & Grafana |
| **Disponibilidade** | Uptime Kuma |

---

## 📊 Planejamento Financeiro (FinOps)

Como diferencial de consultoria, este projeto inclui uma análise de custos operacionais (estimativa baseada na região `us-east-1`):

| Recurso Cloud | Configuração | Custo/Hora | Custo/Mês (Est.) |
| :--- | :--- | :--- | :--- |
| **Amazon EKS** | Control Plane | $0.10 | $72.00 |
| **EC2 Nodes** | 2x t3.medium (4GB RAM) | $0.083 | $59.80 |
| **NAT Gateway** | Saída Privada de Rede | $0.045 | $32.40 |
| **Load Balancer** | Network LB (Ingress) | $0.022 | $16.20 |
| **TOTAL ESTIMADO** | | **$0.25** | **$180.40** |

> 💡 **Valor Consultivo:** O uso da versão 1.29 do Kubernetes evita taxas de suporte estendido da AWS ($0.60/h), gerando uma economia direta de aproximadamente **$432.00 mensais**.

---

## 🚀 Como este ambiente é implantado

1.  **Provisionamento de Infraestrutura:** 
    Navegue até a pasta `live/dev/` e execute `terragrunt run-all apply`.
2.  **Bootstrap da Plataforma:**
    Instale o Argo CD via Helm e aplique o manifesto em `kubernetes/bootstrap/root-app.yaml`.
3.  **Sincronização Automática:**
    O Argo CD assumirá o controle e provisionará automaticamente o Ingress-Nginx, Cert-Manager, Rancher e a stack de monitoramento.

---

## 👤 Autor

**Felipe Carpanezi**
*Cloud Architect & Platform Engineer*

*   [LinkedIn](https://www.linkedin.com/in/felipe-carpanezi-b5440334/)
*   [GitHub](https://github.com/Felipe-carpanezi)