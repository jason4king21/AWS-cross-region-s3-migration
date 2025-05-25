from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS
from diagrams.aws.integration import SQS
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import Glue, Athena



with Diagram("S3–S3 Cross Region Migration Project", show=False, direction="LR", filename="diagrams/architecture", outformat="png"):
    with Cluster("Source Bucket Region\n(AWS Region us-west-1)"):
        source_bucket = S3("S3 Source Bucket")
        sns_topic = SNS("SNS Topic")

    with Cluster("Target Bucket Region\n(AWS Region us-east-1)"):
        sqs_queue = SQS("SQS Queue")
        lambda_fn = Lambda("Lambda Function")
        target_bucket = S3("S3 Target Bucket")
        glue = Glue("Glue Crawler")
        athena = Athena("Athena")

    # Flow
    source_bucket >> sns_topic >> sqs_queue >> lambda_fn >> target_bucket >> glue >> athena