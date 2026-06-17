# RAD_PEER_REVIEW

> Stores Radiology peer reviews done on radiology reports.

**Description:** RadNet Peer Review  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARBITER_COMMENT_TXT` | VARCHAR(1000) |  |  | Comments entered at the time of the discrepancy review. |
| 2 | `ARBITER_DT_NBR` | DOUBLE | NOT NULL |  | Arbitrated date number used for calculation of other time related dimensions and filters. |
| 3 | `ARBITER_DT_TM` | DATETIME |  |  | Last date and time the discrepancy review was updated. |
| 4 | `ARBITER_ID` | DOUBLE | NOT NULL | FK→ | The last individual that reviewed this peer review in the discrepancy queue. |
| 5 | `ARBITER_MIN_NBR` | DOUBLE | NOT NULL |  | Arbitrated minute number used for calculation of other time related dimensions and filters. |
| 6 | `ARBITER_TZ` | DOUBLE | NOT NULL |  | Time zone associated with ARBITER_DT_TM. |
| 7 | `RAD_PEER_REVIEW_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_PEER_REVIEW table. |
| 8 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The report that is being reviewed. |
| 9 | `RESOLVED_IND` | DOUBLE | NOT NULL |  | Indicates if this peer review has been resolved. If so, no further evaluation or arbitration is necessary. |
| 10 | `REVIEWER_ID` | DOUBLE | NOT NULL | FK→ | The individual who performed the peer review. |
| 11 | `REVIEW_CLASS_CD` | DOUBLE | NOT NULL |  | Summarizes the review. A value assigned to a review to describe an overall opinion as to whether the review is positive, neutral, or negative. |
| 12 | `REVIEW_COMMENT_TXT` | VARCHAR(1000) |  |  | Comments entered for the peer review. |
| 13 | `REVIEW_DT_NBR` | DOUBLE | NOT NULL |  | Reviewed date number used for calculation of other time related dimensions and filters. |
| 14 | `REVIEW_DT_TM` | DATETIME | NOT NULL |  | Date and time at which the peer review was last updated. |
| 15 | `REVIEW_MIN_NBR` | DOUBLE | NOT NULL |  | Reviewed minute number used for calculation of other time related dimensions and filters. |
| 16 | `REVIEW_PRSNL_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of personnel that was selected for the review. |
| 17 | `REVIEW_TZ` | DOUBLE | NOT NULL |  | Time zone associated with REVIEW_DT_TM. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARBITER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `REVIEWER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

