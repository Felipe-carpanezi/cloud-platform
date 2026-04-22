# 🌍 Guia de Adaptação Multi-Cloud (Azure, GCP e OCI)

Este documento fornece as diretrizes para portar esta plataforma de engenharia da **AWS** para outros provedores de nuvem, mantendo a consistência da arquitetura e a filosofia GitOps.

---

## 1. Tabela de Equivalência Técnica

Para replicar a solução, os módulos de infraestrutura (IaC) devem ser substituídos pelos serviços correspondentes em cada provedor:

| Recurso | AWS (Base) | Microsoft Azure | Google Cloud (GCP) | Oracle Cloud (OCI) |
| :--- | :--- | :--- | :--- | :--- |
| **Rede** | VPC | VNet | VPC Network | VCN |
| **Kubernetes** | EKS | AKS | GKE | OKE |
| **Banco de Dados** | RDS | Azure SQL | Cloud SQL | Autonomous DB |
| **Load Balancer** | NLB / ALB | Azure Load Balancer | Cloud Load Balancing | OCI Load Balancer |
| **Object Storage** | S3 | Blob Storage | GCS | Object Storage |

---

## 2. Configuração de Ambiente e Autenticação

Antes de executar o `terragrunt apply`, você deve configurar o CLI e a autenticação do novo provedor no seu terminal Linux (WSL):

### 🔵 Microsoft Azure
1. **Instalação:** `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`
2. **Login:** `az login`
3. **Ajuste no Código:** Altere o bloco `provider "aws"` para `provider "azurerm"` nos arquivos `.tf`.

### 🟢 Google Cloud (GCP)
1. **Instalação:** Siga as instruções oficiais do `google-cloud-sdk`.
2. **Login:** `gcloud auth application-default login`
3. **Ajuste no Código:** Altere o provedor para `provider "google"` e especifique o `project_id`.

### 🔴 Oracle Cloud (OCI)
1. **Instalação:** `bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"`
2. **Login:** `oci setup config` (Exige a criação de uma API Key no console).
3. **Ajuste no Código:** Altere o provedor para `provider "oci"`.

---

## 3. Reestruturação de Pastas (Hierarquia Terragrunt)

Para gerenciar múltiplas nuvens no mesmo repositório, recomenda-se organizar a pasta `live/` da seguinte forma:

```text
live/
├── aws/
│   └── dev/
│       ├── vpc/
│       └── eks/
├── azure/
│   └── dev/
│       ├── vnet/
│       └── aks/
└── gcp/
    └── dev/
        ├── vpc/
        └── gke/