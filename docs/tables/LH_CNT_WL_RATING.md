# LH_CNT_WL_RATING

> This table contains the historical record of changes made to a persons Worklist Rating.

**Description:** Lighthouse Content Worklist Rating  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | The ID of the re-admit worklist related to this rating. |
| 5 | `LH_CNT_WL_RATING_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. |
| 6 | `RATING_REASON_CD` | DOUBLE | NOT NULL |  | Represents the reason the individual increased or decreased the rating for this person. |
| 7 | `RATING_UPDT_DT_TM` | DATETIME | NOT NULL |  | The Date/Time Rating was updated. |
| 8 | `RATING_UPDT_ID` | DOUBLE | NOT NULL |  | Individual that update the rating. |
| 9 | `RATING_VALUE` | DOUBLE | NOT NULL |  | Numerical representation of the persons rating. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_READMIT_WORKLIST_ID` | [LH_CNT_READMIT_WORKLIST](LH_CNT_READMIT_WORKLIST.md) | `LH_CNT_READMIT_WORKLIST_ID` |

