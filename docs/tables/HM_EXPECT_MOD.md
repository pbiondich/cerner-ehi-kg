# HM_EXPECT_MOD

> This table will be used to store expectation series or steps that have been modified (e.g. postponed, expired, or satisfied) for individual patients.

**Description:** This table will store expectation series or steps that have been modified.  
**Table type:** ACTIVITY  
**Primary key:** `EXPECT_MOD_ID`  
**Columns:** 27  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COPY_TO_EXPECT_MOD_ID` | DOUBLE | NOT NULL | FK→ | The id of the expectation modifier row that this row has been copied to |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXPECT_MOD_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify an expectation satisfier. |
| 9 | `EXPECT_SAT_ID` | DOUBLE | NOT NULL | FK→ | This will be used to uniquely identify an expectation satisfier. |
| 10 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation Modifier History table for this modifier. |
| 11 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This is a link to an entry on the LONG_TEXT table. This will be used to store a comment for the modifier. If this field is 0, a comment was not entered. |
| 12 | `MODIFIER_DT_TM` | DATETIME | NOT NULL |  | If the TYPE_FLAG indicates this modifier is a Satisfy, this date will be the date on which the expectation was satisfied. If the TYPE_FLAG indicates it is a Postpone, this date will be the date to which the expectation is postponed to. |
| 13 | `MODIFIER_REASON_CD` | DOUBLE | NOT NULL |  | A code value from code set 30440 (Expire Reason), 30441 (Postpone Reason), 30442 (Refuse Reason), 30443 (Satisfy Reason) that indicates the reason for the action. |
| 14 | `MODIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | A code value from code set 30281 that indicates the type of action. |
| 15 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from the ORGANIZATION table |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is an ID corresponding to the table listed in PARENT_ENTITY_NAME. |
| 17 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This will correspond to either the EXPECT_SERIES, EXPECTATION, or EXPECT_STEP table. |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `SAT_PRSNL_ID` | DOUBLE | NOT NULL |  | This is a "Recorded On Behalf Of" field that allows the user who recorded the modifier to indicate who authorized the modifier. |
| 20 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | This is the date that the action became effective. |
| 21 | `STATUS_IND` | DOUBLE | NOT NULL |  | STATUS INDICATORColumn |
| 22 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the user who took the action |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPY_TO_EXPECT_MOD_ID` | [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `EXPECT_MOD_ID` |
| `EXPECT_SAT_ID` | [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `EXPECT_SAT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [HM_EXPECT_MOD](HM_EXPECT_MOD.md) | `COPY_TO_EXPECT_MOD_ID` |
| [HM_EXPECT_MOD_HIST](HM_EXPECT_MOD_HIST.md) | `EXPECT_MOD_ID` |
| [HM_RECOMMENDATION_ACTION](HM_RECOMMENDATION_ACTION.md) | `EXPECT_MOD_ID` |

