# LH_MU_AGGREGATION

> Contains Lighthouse Meaningful Use metrics that have been aggregated by 7-days, 30-days, 90-days, 12 weeks, and 12 months

**Description:** LH_MU_AGGREGATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACI_EC_GROUP_FLAG` | DOUBLE |  |  | This column mentions whether the data is loaded for EP/CCN - Eligible Provide/CMS Certification Nbr(0) or ACI Group - Advanced Care Information Group (1) or ACI EC - Advanced Care Information Eligible Clinician (2) or EP - Eligible Provider(3) or CCN - CMS Certification Nbr(4). |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Foreign key referencing BR_ELIGIBLE_PROVIDER table |
| 4 | `CALENDAR_YEAR` | DOUBLE |  |  | Represents calendar year (2013, 2014, 2015, etc.) |
| 5 | `CCN_NBR_TXT` | VARCHAR(150) |  |  | The CMS Certification Number (CCN) used to uniquely identify a Facility |
| 6 | `DATE_RANGE_END` | DATETIME |  |  | Identifies the date range the metric is aggregated to |
| 7 | `DATE_RANGE_START` | DATETIME |  |  | Identifies the date range the metric is aggregated to |
| 8 | `DENOMINATOR_CNT` | DOUBLE |  |  | The number of qualifying patients or visits which appears for a Meaningful Use EP measure |
| 9 | `D_BR_CCN_ID` | DOUBLE | NOT NULL |  | Foreign key referencing LH_D_BR_CCN table |
| 10 | `ED_RPT_METHOD_FLG` | DOUBLE |  |  | Identifies which ED definition the records falls in and how it should be processed when the Report is ran. 0 - N/A 1 - All ED Visits 2 - Observation Services |
| 11 | `EP_NAME` | VARCHAR(100) |  |  | Represents the name of the eligible provider |
| 12 | `EXCEPTION_CNT` | DOUBLE |  |  | The number of exceptions. |
| 13 | `EXCLUSION_CNT` | DOUBLE |  |  | The number of qualifying patients or visits which are excluded from Meaningful Use EP measure |
| 14 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 15 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 16 | `GPRO_NAME` | VARCHAR(255) |  |  | Group practice name of the TIN if the ACI_EC_GROUP_FLAG is 1 or 2 (ACI Group or ACI EC). |
| 17 | `GPRO_TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Group practice tax identification number in text format. |
| 18 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 19 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 20 | `IPP_CNT` | DOUBLE | NOT NULL |  | Initial patient population count. |
| 21 | `LAST_MU_LOAD_DT_TM` | DATETIME |  |  | Max extract_dt_tm of LH_AMB_QUAL_ENCNTR for the period number |
| 22 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 23 | `LH_MU_AGGREGATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_AGGREGATION table. |
| 24 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 25 | `METRIC_NAME` | VARCHAR(500) |  |  | Name that uniquely identifies that Metric being aggregated. This could be one of the 18 Functional measures or any of the Stroke, ED Throughput, or VTE measures |
| 26 | `METRIC_VALUE` | DOUBLE |  |  | Calculated value that represents the average of the metric by the date range specified |
| 27 | `MSR_POP_CNT` | DOUBLE | NOT NULL |  | Measure population count. |
| 28 | `MU_VERSION` | DOUBLE |  |  | Numeric representation of Meaningful Use version (e.g. "1" stands for stage I and "2" for stage II) |
| 29 | `NPI_NBR_TXT` | VARCHAR(200) |  |  | The National Provider Identification used to uniquely identify a Eligible Provider |
| 30 | `NUMERATOR_CNT` | DOUBLE |  |  | The number of qualifying patients or visits which meet the criteria (MET/DONE) for Meaningful Use EP measure |
| 31 | `PERIOD_NBR` | DOUBLE | NOT NULL |  | Number to denote the script specific date range for this record. |
| 32 | `SCRIPT_VERSION` | VARCHAR(50) |  |  | The name of script which populated this row (e.g. "lh_nqf_aggregation.prg", "lh_nqf2_aggregation.prg", etc.) |
| 33 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 36 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

