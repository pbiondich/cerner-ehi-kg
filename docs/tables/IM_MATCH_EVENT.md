# IM_MATCH_EVENT

> IM Match Event

**Description:** This table contains a log of match and unmatch events that have occurred.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IM_ACQUIRED_STUDY_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_ACQUIRED_STUDY table. It identifies the acquired study that has been matched / unmatched. |
| 2 | `IM_MATCH_EVENT_ID` | DOUBLE | NOT NULL |  | This column contains a meaningless number that only serves to uniquely identify a row. |
| 3 | `IM_SERIES_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the IM_SERIES table. It uniquely identifies the series. |
| 4 | `IM_STUDY_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_STUDY table. It identifies the study row that has been matched/unmatched. |
| 5 | `MATCH_EVENT_CD` | DOUBLE | NOT NULL |  | This column indicates what event took place. (match/unmatch) |
| 6 | `MATCH_PRSNL_ID` | DOUBLE | NOT NULL |  | This column contains a foreign key to the PRSNL table. It identifies the user that performed the match/unmatch if it was done manually. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_ACQUIRED_STUDY_ID` | [IM_ACQUIRED_STUDY](IM_ACQUIRED_STUDY.md) | `IM_ACQUIRED_STUDY_ID` |
| `IM_SERIES_ID` | [IM_SERIES](IM_SERIES.md) | `IM_SERIES_ID` |
| `IM_STUDY_ID` | [IM_STUDY](IM_STUDY.md) | `IM_STUDY_ID` |

