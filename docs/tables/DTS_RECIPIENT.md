# DTS_RECIPIENT

> This table stores information on each recipient who has been marked to receive a copy of the mail merged document.

**Description:** Dictation Transcription Recipient  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS_HIST_ID` | DOUBLE | NOT NULL |  | The address effective for this associated event_prsnl_id. |
| 2 | `DTS_RECIPIENT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DTS_RECIPIENT table. |
| 3 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The event_prsnl_id that this associated address pertains to. |
| 4 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Indicates the relationship between the personnel and the document. 0 - Personnel is not a primary recipient, 1 - Personnel is the primary recipient. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PRSNL_ID` | [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `CE_EVENT_PRSNL_ID` |

