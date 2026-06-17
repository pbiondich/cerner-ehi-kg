# ENCNTR_LEGAL_REVIEW_R

> This table will hold the relationship between legal statuses and Review Board history records

**Description:** Encounter Legal Status Review Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DECISION_CD` | DOUBLE | NOT NULL |  | Decision reached by the review board, e.g. GUILTY, NOT GUILTY Code Set 29445. |
| 2 | `DISPOSITION_RECVD_DT_TM` | DATETIME |  |  | The date and time the disposition was received |
| 3 | `ENCNTR_LEG_STAT_REV_R_ID` | DOUBLE | NOT NULL |  | The unique identifier for the ENCNTR_LEGAL_STATUS_REV_R table |
| 4 | `HEARING_DT_TM` | DATETIME |  |  | The date and time of the hearing |
| 5 | `LEGAL_RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | The recommended legal action |
| 6 | `LEGAL_STATUS_R_ID` | DOUBLE | NOT NULL | FK→ | Inherited Identifier for rows associated to the ENCNTR_LEGAL_STATUS_R table |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the Hearing |
| 8 | `OTHER_RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | Other recommended Legal action |
| 9 | `REASON_RECVD_DT_TM` | DATETIME |  |  | The Date and Time the reason was received |
| 10 | `RECOMMENDATION_CD` | DOUBLE | NOT NULL |  | Recommended action |
| 11 | `REVIEW_BOARD_CD` | DOUBLE | NOT NULL |  | The facility defined review board code |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LEGAL_STATUS_R_ID` | [ENCNTR_LEGAL_STATUS_R](ENCNTR_LEGAL_STATUS_R.md) | `LEGAL_STATUS_R_ID` |

