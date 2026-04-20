from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, InternetGateway, NATGateway, ELB
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM
from diagrams.onprem.client import User

# Configurações de exibição
graph_attr = {
    "fontsize": "20",
    "bgcolor": "white"
}

with Diagram("Cloud Platform - Full Architecture", show=False, filename="full_architecture", direction="LR", graph_attr=graph_attr):

    user = User("Client Access")

    with Cluster("AWS Region: us-east-1"):
        igw = InternetGateway("IGW")
        
        with Cluster("VPC (10.0.0.0/16)"):
            
            with Cluster("Public Subnets Layer"):
                with Cluster("Subnet Public 1 (10.0.1.0/24)"):
                    lb = ELB("NLB (3.223.58.250)")
                    nat = NATGateway("NAT Gateway")
                
            with Cluster("Private Subnets Layer (EKS Nodes)"):
                with Cluster("Subnet Private 1 (10.0.3.0/24)"):
                    eks_nodes = [EC2("Node 1 (t3.medium)"),
                                 EC2("Node 2 (t3.medium)")]
            
            eks_control_plane = EKS("EKS Control Plane (v1.29)")

            with Cluster("Platform Services (Kubernetes)"):
                rancher = Cloudwatch("Rancher (Management)")
                argo = IAM("ArgoCD (GitOps)")
                grafana = Cloudwatch("Grafana (Obs)")

    # Fluxo de Rede
    user >> Edge(label="https://rancher.IP.sslip.io") >> lb
    lb >> igw
    igw >> nat
    nat >> eks_nodes
    
    # Controle do EKS
    eks_control_plane >> eks_nodes
    eks_nodes >> argo
    eks_nodes >> rancher
    eks_nodes >> grafana