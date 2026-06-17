# CDI_BATCH_SUMMARY

> The CDI Batch Summary table

**Description:** CDI Batch Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AC_QC_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture QC module. |
| 2 | `AC_REC_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture Recognition module. |
| 3 | `AC_REL_CNT` | DOUBLE |  |  | Number of documents in the batch released from Ascent Capture. |
| 4 | `AC_REL_DT_TM` | DATETIME |  |  | Date and time the batch was released from Ascent Capture. |
| 5 | `AC_REL_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture Release module. |
| 6 | `AC_SCAN_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture Scan module. |
| 7 | `AC_VALID_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture Validation module. |
| 8 | `AC_VERIFY_TIME` | DOUBLE |  |  | Time (in seconds) the batch spend in the Ascent Capture Verification module. |
| 9 | `AUTO_COMP_CNT` | DOUBLE |  |  | Total number of documents that were processed through the auto index queue. |
| 10 | `CDI_AC_BATCH_ID` | DOUBLE | NOT NULL | FK→ | AC Batch Identifier. Foreign key back to parent table CDI_AC_BATCH |
| 11 | `CDI_BATCH_SUMMARY_ID` | DOUBLE | NOT NULL |  | Primary key for this table. |
| 12 | `COMBINED_CNT` | DOUBLE |  |  | Number of documents combined away. |
| 13 | `COMPLETE_CNT` | DOUBLE |  |  | Number of complete documents in the batch. |
| 14 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 15 | `CUR_AUTO_CNT` | DOUBLE |  |  | Number of documents from the batch in the auto index queue. |
| 16 | `CUR_MAN_CNT` | DOUBLE |  |  | Number of documents from the batch in the manual index queue. |
| 17 | `ECP_CNT` | DOUBLE |  |  | Number of cover pages removed. |
| 18 | `EXTERNAL_BATCH_IDENT` | DOUBLE | NOT NULL |  | External batch identifier value |
| 19 | `MAN_COMP_CNT` | DOUBLE |  |  | Total number of documents that were processed through the manual index queue. |
| 20 | `MAN_CREATE_CNT` | DOUBLE |  |  | Number of documents created in the manual index queue. |
| 21 | `MAN_DEL_CNT` | DOUBLE |  |  | Number of documents deleted in the manual index queue. |
| 22 | `PHARMACY_CNT` | DOUBLE | NOT NULL |  | Number of documents from the bacth currently in the pharmacy queue. |
| 23 | `PHARMACY_COMP_CNT` | DOUBLE | NOT NULL |  | Total number of documents from the batch that have been completed in the pharmacy queue |
| 24 | `PHARMACY_DEL_CNT` | DOUBLE | NOT NULL |  | Number of documents from the batch deleted in the pharmacy queue |
| 25 | `PREP_COMP_CNT` | DOUBLE |  |  | Number of documents processed through the batch preparation queue. |
| 26 | `TOT_AUTO_TIME` | DOUBLE |  |  | Total time all documents spent in the auto index queue (in Sec). Divide by AUTO_COMP_CNT to get average time spent in the queue. |
| 27 | `TOT_MAN_TIME` | DOUBLE |  |  | Total time all documents spent in the manual index queue (in sec). Divide by AUTO_COMP_CNT to get average time spent in the queue. |
| 28 | `TOT_PHARMACY_TIME` | DOUBLE | NOT NULL |  | Total time all documents from the batch spent in the pharmacy queue. Divide by pharmacy_comp_cnt for the average time. |
| 29 | `TOT_PREP_TIME` | DOUBLE |  |  | Total time all documents spent in the batch preparation queue (in Sec). Divide by AUTO_COMP_CNT to get average time spent in the queue. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `WQM_CREATE_CNT` | DOUBLE | NOT NULL |  | Number of documents created in Work Queue Management. |
| 36 | `WQM_DEL_CNT` | DOUBLE | NOT NULL |  | Number of documents deleted in Work Queue Management. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_AC_BATCH_ID` | [CDI_AC_BATCH](CDI_AC_BATCH.md) | `CDI_AC_BATCH_ID` |

