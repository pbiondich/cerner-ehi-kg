# CODED_EXAM_REASON

> The Coded_Exam_Reason table contains a list of reasons for exam that can be chosen from at the time that the order is placed.

**Description:** Coded Exam Reason  
**Table type:** REFERENCE  
**Primary key:** `EXAM_REASON_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | The Description contains the reason for exam that will appear in pick lists. |
| 3 | `DISCIPLINE_TYPE_CD` | DOUBLE | NOT NULL |  | This column identifies the discipline or product that the reason is built for. This will be 0 if it is a common reason used by all teams. |
| 4 | `EXAM_REASON_ID` | DOUBLE | NOT NULL | PK | The exam_reason_id is a unique, meaningless number that serves only as a unique identifier for the coded exam reason. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXAM_REASON](EXAM_REASON.md) | `EXAM_REASON_ID` |

