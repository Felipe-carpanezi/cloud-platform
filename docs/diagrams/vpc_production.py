from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, InternetGateway, NATGateway
from diagrams.aws.compute import EC2

with Diagram("AWS VPC Production Architecture", show=True):

    igw = InternetGateway("Internet Gateway")

    with Cluster("VPC"):

        with Cluster("Public Subnets"):
            public1 = PublicSubnet("Public Subnet 1")
            public2 = PublicSubnet("Public Subnet 2")

        with Cluster("Private Subnets"):
            private1 = PrivateSubnet("Private Subnet 1")
            private2 = PrivateSubnet("Private Subnet 2")

        nat = NATGateway("NAT Gateway")

        app1 = EC2("App 1")
        app2 = EC2("App 2")

    # Fluxo
    igw >> public1
    igw >> public2

    public1 >> nat
    nat >> private1
    nat >> private2

    private1 >> app1
    private2 >> app2