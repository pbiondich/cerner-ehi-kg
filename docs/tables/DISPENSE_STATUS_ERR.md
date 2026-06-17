# DISPENSE_STATUS_ERR

> This Table contains the error information for any prescription that does not make it through the Inbound Baker Interface process. (non-reference, purgable)

**Description:** This table contains the error information for the Inbound Interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPLETED_DT_TM` | DATETIME | NOT NULL |  | This is the date and time the Dispense actually completes (i.e. recovery is completed). |
| 6 | `COMPLETED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `COMPLETED_USER_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that corrected the error(s) and completed the dispense. |
| 8 | `DISPENSE_ERR_CD` | DOUBLE | NOT NULL |  | Identifies the type of Error that has occurred. |
| 9 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies related dispense transaction that the error occurred on. From the Dispense_Hx table. |
| 10 | `DISPENSE_QTY` | DOUBLE | NOT NULL |  | This represents the number of a particular drug to dispense. |
| 11 | `DISPENSE_STATUS_CD` | DOUBLE | NOT NULL |  | This reflects the status of the Dispense Event. |
| 12 | `DISPENSE_STATUS_ERR_ID` | DOUBLE | NOT NULL |  | Unique Identifier to identify a particular dispense_status_err record. |
| 13 | `POSTED_DT_TM` | DATETIME | NOT NULL |  | This is the date and time the user first corrected the error. |
| 14 | `POSTED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

