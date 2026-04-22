import os
from urllib.request import urlretrieve, Request, urlopen
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.compute import Pod

# Links Oficiais e Estáveis (GitHub Avatars/CDNs)
logos = {
    "argocd": "https://avatars.githubusercontent.com/u/30242303?s=200&v=4",
    "rancher": "https://avatars.githubusercontent.com/u/9343010?s=200&v=4",
    "kuma": "https://avatars.githubusercontent.com/u/81578330?s=200&v=4",
    "certmanager": "https://avatars.githubusercontent.com/u/36535414?s=200&v=4"
}

def download_logos():
    for name, url in logos.items():
        filename = f"{name}.png"
        if not os.path.exists(filename):
            print(f"Baixando logo: {name}...")
            try:
                # Simula um navegador para evitar bloqueio de bot
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urlopen(req) as response, open(filename, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Erro ao baixar {name}: {e}")

download_logos()

graph_attr = {
    "fontsize": "25",
    "bgcolor": "white",
    "pad": "0.5"
}

with Diagram("Kubernetes - Enterprise Software Stack", show=False, filename="cluster_internal_pro", graph_attr=graph_attr):
    
    ingress = Ingress("Nginx Ingress\n(Traffic Gateway)")

    with Cluster("Platform Layer (Governance)"):
        argo = Custom("ArgoCD\n(GitOps)", "./argocd.png")
        rancher = Custom("Rancher\n(Management)", "./rancher.png")
        cert = Custom("Cert-Manager\n(Security)", "./certmanager.png")

    with Cluster("Application Layer (Business)"):
        with Cluster("Namespace: my-app"):
            app_svc = Service("Web Service")
            app_pod = Pod("HTML Page\n(Nginx)")
        
        with Cluster("Namespace: uptime-kuma"):
            kuma = Custom("Uptime Kuma\n(SRE)", "./kuma.png")

    # Fluxo de Tráfego de Usuário
    ingress >> Edge(color="darkblue", label="HTTPS") >> rancher
    ingress >> Edge(color="darkblue") >> kuma
    ingress >> Edge(color="darkgreen", label="HTTP") >> app_svc >> app_pod
    
    # ArgoCD gerencia o estado de tudo
    argo >> Edge(style="dashed", color="red", label="Sync") >> [rancher, kuma, app_pod, cert]