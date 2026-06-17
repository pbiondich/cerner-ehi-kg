# SA_ANESTHESIA_REC_STATUS

> Contains records for when an anesthesia records status changes (unfinalized,finalized,etc) 1 record each time an anesthesia record is finalized or unfinalized. Estimate 2:1 with SA_ANESTHESIA_RECORD. 52,200

**Description:** SA Anesthesia Record Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PRINT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Used to indicate whether the billing summary needs to be printed for the anesthesia record. 0 = not printed; 1 = printed; 2 = needs to be re-printed. |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL |  | User that changed the status of the anesthesia record |
| 7 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The Anesthesia Record that the status refers to |
| 8 | `SA_ANESTHESIA_REC_STATUS_ID` | DOUBLE | NOT NULL |  | Unique value to the anesthesia record status record |
| 9 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | Date/Time the status of the anesthesia record was changed |
| 10 | `STATUS_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines status of anesthesia record (0=finalized, 1=unfinalized) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |

