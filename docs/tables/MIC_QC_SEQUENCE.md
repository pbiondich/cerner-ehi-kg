# MIC_QC_SEQUENCE

> This reference table contains a record for each microbiology QC sequence.

**Description:** Microbiology Quality Control Sequence  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_TIME_NBR` | DOUBLE | NOT NULL |  | This field contains the time of day that a sequence begins. |
| 6 | `END_TIME_NBR` | DOUBLE | NOT NULL |  | This field contains the time of day that a sequence ends. |
| 7 | `SEQUENCE_ID` | DOUBLE | NOT NULL |  | This field contains the unique value that identifies the QC sequence. |
| 8 | `SEQUENCE_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the unique name for the QC sequence. |
| 9 | `SEQUENCE_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field is the same as the sequence_name field, only converted to uppercase. |
| 10 | `SEQUENCE_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | SEQUENCE_NAME_KEY_A_NLS column |
| 11 | `SEQUENCE_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | This field is 2 times the length of the key + 2. It is used for sorting the name field when in a non-English environment. |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the service resource code associated with the sequence. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

