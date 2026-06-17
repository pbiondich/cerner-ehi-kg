# LH_CNT_ADVSR_EVENT

> This table will be used to track advisor events for the Infection Control Uplift Advisor.

**Description:** LH_CNT_ADVSR_EVENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADV_EVENT_DT_TM` | DATETIME |  |  | This is used to flex the Advisor release rules for the advisor. This will be the time that we will report the event off of. This date swings the release version. |
| 3 | `ADV_SPECIFIC_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | This will store the specific event type |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LONG_TEXT table that will store the contents of the comments field in the advisor |
| 6 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LH_CNT_ADVSR_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_ADVSR_EVENT table. |
| 9 | `UNCHART_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LONG_TEXT table that will store the text when the user uncharts the advisor |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `UNCHART_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

