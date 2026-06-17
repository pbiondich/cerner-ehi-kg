# LH_MU_EP_METRICS_RELTN

> Fact table for Meaningful Use Lighthouse Report.

**Description:** LH_MU_EP_METRICS_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_EP_IND` | DOUBLE |  |  | Identifies the encounter and EP relationship is base on billing system. |
| 2 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | The ID of the row on the BR_ELIGIBLE_PROVIDER table that is related to the MU FX Metric. |
| 3 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Identifies the type of encounter personnel relationship. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LH_MU_EP_METRICS_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_EP_METRICS_RELTN table. |
| 10 | `LH_MU_FX_METRICS_ID` | DOUBLE | NOT NULL |  | The ID of the row on the LH_MU_FX_METRICS table that is related to the BR_ELIGIBLE_PROVIDER table. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source of the update. |
| 14 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

