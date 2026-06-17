# PFT_UMDAP_QUESTION

> This table stores the answers to UMDAP related questions.

**Description:** PFT UMDAP QUESTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ANSWER_AMT` | DOUBLE | NOT NULL |  | Dollar amount returned by the user. |
| 6 | `PFT_UMDAP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to PFT_UMDAP |
| 7 | `PFT_UMDAP_QUESTION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `PFT_UMDAP_QUES_CD` | DOUBLE | NOT NULL |  | This code value relates to the specific umdap question answered by the user. Not every question needs to be answered for a set. |
| 9 | `PFT_UMDAP_QUES_GRP_CD` | DOUBLE | NOT NULL |  | This code value relates to the grouping mechanism for the UMDAP questions code set. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_UMDAP_ID` | [PFT_UMDAP](PFT_UMDAP.md) | `PFT_UMDAP_ID` |

