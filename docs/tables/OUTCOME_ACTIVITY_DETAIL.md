# OUTCOME_ACTIVITY_DETAIL

> Used to store the detials of outcomes

**Description:** Outcome Activity Detail  
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
| 4 | `OUTCOME_ACTIVITY_DETAIL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `OUTCOME_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key for this table and also the unique identifier for rows on the OUTCOME_ACTIVITY table. |
| 6 | `OUTCOME_DETAIL_DISPLAY` | VARCHAR(255) |  |  | the display value of the outcome detail |
| 7 | `OUTCOME_DETAIL_DT_TM` | DATETIME |  |  | outcome detail field date time value |
| 8 | `OUTCOME_DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type code of detail. For example outcome_sub_type,outcome_category_cd, outcome_frequency |
| 9 | `OUTCOME_DETAIL_VALUE` | DOUBLE |  |  | Value of the outcome detail if a numeric or coded value. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTCOME_ACTIVITY_ID` | [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `OUTCOME_ACTIVITY_ID` |

