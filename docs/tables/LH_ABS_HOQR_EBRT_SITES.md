# LH_ABS_HOQR_EBRT_SITES

> Contains information for treatment sites in HOQR EBRT condition

**Description:** LH_ABS_HOQR_EBRT_SITES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 3 | `EXCLUDE_33_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'excluded' |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LH_ABS_HOQR_EBRT_SITES_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HOQR_EBRT_SITES table. |
| 10 | `METRIC_TXT` | VARCHAR(20) |  |  | Identifies specific metric for category |
| 11 | `NOCORDCOMP_FLAG` | DOUBLE |  |  | Identifies if there is no spinal cord compression, cauda, equina compression or radicular pain |
| 12 | `NOFEMCORT_FLAG` | DOUBLE |  |  | Identifies if there was no femoral axis cortical involvement > 3 cm in length |
| 13 | `NOHXRAD_FLAG` | DOUBLE |  |  | Identifies if patient has history of previous radiation therapy to same anatomic site |
| 14 | `NOSURGSTAB_FLAG` | DOUBLE |  |  | Identifies if the patient did not undergo a surgical stabilization procedure |
| 15 | `NUMERATOR_33_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'met' or 'not met' |
| 16 | `OTHERBONEMET_FLAG` | DOUBLE |  |  | Identifies if EBRT treatment was used to treat anything other than bone metastases |
| 17 | `OTHERPTRSN_FLAG` | DOUBLE |  |  | Identifies if there are specified patient reasons treatment was declined at the current EBRT treatment site (economic, social, religious, or other documented patient reasons). |
| 18 | `REASON_TXT` | VARCHAR(100) |  |  | The Metric's category reason |
| 19 | `REJECT_33_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'rejected' |
| 20 | `RXEBRT_FLAG` | DOUBLE |  |  | Identifies if one of the recommended fractionation schemes was prescribed |
| 21 | `SITE_SEQ` | DOUBLE |  |  | The sequence number of the treatment site. |
| 22 | `SITE_TXT` | VARCHAR(150) |  |  | Identifies the EBRT tratement site |
| 23 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the reecord. |
| 27 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

