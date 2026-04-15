from diagrams import Diagram, Cluster
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3

with Diagram("Cloud Architecture - Production Ready", show=True):

    dns = Route53("Route53")

    with Cluster("Edge Layer"):
        cdn = CloudFront("CloudFront")

    with Cluster("Application Layer"):
        frontend = EC2("Frontend")
        backend = EC2("Backend")

    with Cluster("Data Layer"):
        db = RDS("PostgreSQL")
        storage = S3("Assets")

    webhook = Lambda("Webhook")

    dns >> cdn >> frontend >> backend
    backend >> db
    backend >> storage
    backend >> webhook