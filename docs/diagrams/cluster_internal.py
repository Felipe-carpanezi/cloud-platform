from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.custom import Custom

# Configurações visuais
graph_attr = {
    "fontsize": "25",
    "bgcolor": "white",
    "splines": "ortho"
}

with Diagram("EKS - Arquitetura Interna de Software", show=False, filename="cluster_internal", graph_attr=graph_attr):
    
    ingress_gateway = Ingress("Nginx Ingress\nController")

    with Cluster("Namespace: argocd"):
        argo = Pod("ArgoCD Server")
        argo_repo = Pod("Repo Server")

    with Cluster("Namespace: cattle-system"):
        rancher = Pod("Rancher Manager")

    with Cluster("Namespace: cert-manager"):
        cert = Pod("Cert-Manager")

    with Cluster("Namespace: my-app"):
        web_svc = Service("Web Service")
        web_pods = [Pod("HTML App (Replica 1)")]

    with Cluster("Namespace: uptime-kuma"):
        kuma = Pod("Uptime Kuma")

    # Definindo as conexões
    ingress_gateway >> Edge(color="darkblue") >> rancher
    ingress_gateway >> Edge(color="darkblue") >> kuma
    ingress_gateway >> Edge(color="darkgreen") >> web_svc >> web_pods
    
    # O ArgoCD "observa" tudo, mas não flui tráfego de usuário por ele
    argo >> Edge(style="dashed") >> argo_repo