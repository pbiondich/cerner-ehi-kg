# HM_EXPECT_MOD_HIST

> This is a history table for the HM_EXPECT_MODIFIER table.

**Description:** This is a history table for the EXPECT_MODIFIER table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | ACTION DATE/TIMEColumn |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | This is the number of the action that was taken. It will be incremented each time a new action is performed. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the action that was performed. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXPECT_MOD_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECT_MODIFIER table that indicates which modifier this record corresponds to. |
| 11 | `EXPECT_SAT_ID` | DOUBLE | NOT NULL | FK→ | This will be used to uniquely identify an expectation satisfier. |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This is a link to an entry on the LONG_TEXT table. This will be used to store a comment for the modifier. If this field is 0, a comment was not entered. |
| 13 | `MIGRATED_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the data has been analyzed for migration to the HM_RECOMMENDATION_ACTION table.0 = No; 1 = Yes; 2 = Ignored |
| 14 | `MODIFIER_DT_TM` | DATETIME | NOT NULL |  | If the TYPE_FLAG indicates this modifier is a Satisfy, this date will be the date on which the expectation was satisfied. If the TYPE_FLAG indicates it is a Postpone, this date will be the date to which the expectation is postponed to. |
| 15 | `MODIFIER_REASON_CD` | DOUBLE | NOT NULL |  | A code value from code set 30440 (Expire Reason), 30441 (Postpone Reason), 30442 (Refuse Reason), 30443 (Satisfy Reason) that indicates the reason for the action.. |
| 16 | `MODIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | A code value from code set 30281 that indicates the type of action. |
| 17 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from the ORGANIZATION table. |
| 18 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is an ID corresponding to the table listed in PARENT_ENTITY_NAME. |
| 19 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This will correspond to either the EXPECT_SERIES, EXPECTATION, or EXPECT_STEP table. |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 21 | `RECOMMENDATION_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from the HM_RECOMMENDATION_ACTION table |
| 22 | `SAT_PRSNL_ID` | DOUBLE | NOT NULL |  | This is a "Recorded On Behalf Of" field that allows the user who recorded the modifier to indicate who authorized the modifier. |
| 23 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | This is the date that the action became effective. |
| 24 | `STATUS_IND` | DOUBLE | NOT NULL |  | STATUS INDICATORColumn |
| 25 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the user who took the action |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_MOD_ID` | [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `EXPECT_MOD_ID` |
| `EXPECT_SAT_ID` | [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `EXPECT_SAT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RECOMMENDATION_ACTION_ID` | [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `RECOMMENDATION_ACTION_ID` |

