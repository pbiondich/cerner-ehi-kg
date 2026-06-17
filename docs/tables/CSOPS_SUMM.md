# CSOPS_SUMM

> This table holds an audit of all the runs of the Charge Services interface scripts.

**Description:** CS Operations Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMOUNT` | DOUBLE |  |  | Sum of the prices of all the charges for the job_name_cd and interface_file_id on that row. |
| 2 | `BATCH_NUM` | DOUBLE |  |  | The batch number of the charges for that job_name_cd and interface_file_id. The batch_num comes from the batch_num field on the interface_charge table. |
| 3 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | This value will be the code value from code set 13028 with a cdf_meaning of DEBIT or CREDIT. |
| 4 | `CSOPS_SUMM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the csops_summ table. It is an internal system assigned number. |
| 5 | `END_DT_TM` | DATETIME |  |  | This field holds the date and time that the job_name_cd completed. |
| 6 | `INTERFACE_FILE_ID` | DOUBLE | NOT NULL |  | This field holds the interface_file_id from the interface_file table for the charges that were processed by the job_name_cd. |
| 7 | `JOB_NAME_CD` | DOUBLE | NOT NULL |  | This field holds the code value from code set 25632 that tells what script was running for this particular row. |
| 8 | `JOB_STATUS` | VARCHAR(1) |  |  | This field either holds the value of F for failure, S for success or Z for nothing processed, depending on the status that the job_name_cd returns. |
| 9 | `QUANTITY` | DOUBLE |  |  | This field holds the sum of all the quantities of the charges for the job_name_cd and interface_file_id. |
| 10 | `RAW_COUNT` | DOUBLE |  |  | This field holds the number of charge rows that were processed by the job_name_cd. |
| 11 | `SEQUENCE` | DOUBLE |  |  | If the job_name_cd is AFC_RUN_CUSTOM and the interface_file_id has the hl7_ind checked, then the charges were processed in batches of 1000. This field holds the sequentialnumber of that batch. So if it is the first batch of 1000 charges, this field would contain a value of 1. |
| 12 | `START_DT_TM` | DATETIME |  |  | This field holds the date and time that the job_name_cd started. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

