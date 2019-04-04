import logging

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'b2fpicklist'

job_config = bigquery.QueryJobConfig()
# Set the destination table
sql = """
SELECT * `mtech-daas-transact-sdata-dev.rfnd_sls_v.OC_SALES_PROD_LOC_WK_V` LIMIT 10;
"""

# Start the query, passing in the extra configuration.
queryjob = client.query(
    sql,
    # Location must match that of the dataset(s) referenced in the query
    # and of the destination table.
    location='US',
    job_config=job_config)  # API request - starts the query

data = queryjob.result()  # Waits for the query to finish
print(list(data))


