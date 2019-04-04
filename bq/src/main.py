import logging

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'b2fpicklist'

job_config = bigquery.QueryJobConfig()
# Set the destination table
sql = """
select ab.PROD_DIM_ID,ab.AMC_WEEK_KEY,ab.END_DATE,ab.DEPT_NBR,cast(ab.SALE_UNITS as FLOAT64) as SALE_UNITS,cast(ab.SALE_PRICE as FLOAT64) as SALE_PRICE,ab.SKU_UPC_NBR ,ab.ZL_STAT_NBR,ab.DIVN_NBR,ab.LOC_DIM_ID,CURRENT_DATE as LOAD_DATE from
(SELECT  sl.prod_dim_id,sl.loc_dim_id,sl.divn_nbr,tp.amc_week_key,sl.greg_amc_week_end_dt  end_date,sl.dept_nbr,sum(sls_units) as SALE_UNITS,sum(sl.sls_mdse_amt)/sum(sls_units) as SALE_PRICE ,
(case when pd.sku_upc_nbr=0 then sl.prod_dim_id else pd.sku_upc_nbr end) as SKU_UPC_NBR ,
sl.zl_stat_nbr from  `mtech-daas-transact-sdata-dev.rfnd_sls_v.OC_SALES_PROD_LOC_WK_V` sl
inner join `mtech-daas-reference-pdata-dev.trst_ref_v.AMC_WEEK_V` tp on sl.greg_amc_week_end_dt= tp.greg_amc_week_end_dt
left join
(select t1.prod_dim_id,t1.loc_dim_id,t1.dept_nbr,max(t1.greg_amc_week_end_dt) as check_amc from  `mtech-daas-transact-sdata-dev.rfnd_sls_v.OC_SALES_PROD_LOC_WK_V`  t1
where  t1.loc_dim_id  in(8750,8526,3534,7905,480,8464,8753,8529,8390,7950)  and t1.divn_nbr in (12,13) and t1.fil_rplnsh_flg='N' group by  t1.prod_dim_id,t1.loc_dim_id,t1.dept_nbr)  t2
on sl.prod_dim_id=t2.prod_dim_id and sl.dept_nbr=t2.dept_nbr and sl.loc_dim_id=t2.loc_dim_id
inner join `mtech-daas-product-pdata-dev.trst_prod_v.PROD_DIM_V`  pd on sl.prod_dim_id=pd.prod_dim_id and sl.dept_nbr=pd.dept_nbr
inner join `mtech-daas-facility-pdata-dev.trst_fclty_v.LOCN_DIM_V` ld on sl.loc_dim_id=ld.loc_dim_id
inner join  `mtech-daas-product-pdata-dev.trst_prod_v.MCH_HEIR_V` mch on mch.dept_nbr=sl.dept_nbr and mch.divn_nbr=sl.divn_nbr
and mch.mgm_id not in (6464,7906,1005,1204,4700,3401,1204,6203,3303,6201)
and mch.parent_div_id not in (0,60,65) and mch.dept_nbr not in (75,90,116,147,182,208,236,438,514,518,519,521,604,612,638,655,681,697,707,708,747,773,815,816)
where sl.loc_dim_id in(8750,8526,3534,7905,480,8464,8753,8529,8390,7950) and sl.divn_nbr in (12,13) and sl.greg_amc_week_end_dt between '2017-06-01' and '2018-11-16' and pd.end_dt  = '3000-01-01'  and ld.end_dt='3000-01-01'
group by sl.prod_dim_id,sl.loc_dim_id,tp.amc_week_key,sl.dept_nbr,sl.zl_stat_nbr,sl.divn_nbr,pd.sku_upc_nbr,t2.check_amc,sl.greg_amc_week_end_dt
having sum(sls_units)>0 and t2.check_amc >='2018-01-01') ab LIMIT 5;
"""

# Start the query, passing in the extra configuration.
query_job = client.query(
    sql,
    # Location must match that of the dataset(s) referenced in the query
    # and of the destination table.
    location='US',
    job_config=job_config)  # API request - starts the query

data = query_job.result()  # Waits for the query to finish
print(list(data))


