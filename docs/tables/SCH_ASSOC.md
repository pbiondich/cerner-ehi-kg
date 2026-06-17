# SCH_ASSOC

> Scheduling Generic Association

**Description:** SCH_ASSOC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSOCIATION_ID` | DOUBLE | NOT NULL |  | Scheduling Association Identifier |
| 6 | `ASSOC_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the Scheduling Association Type |
| 7 | `ASSOC_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Association Type Code |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `CHILD_ID` | DOUBLE | NOT NULL |  | Child Identifier |
| 11 | `CHILD_MEANING` | VARCHAR(12) |  |  | Child Meaning |
| 12 | `CHILD_TABLE` | VARCHAR(32) |  |  | Child Table |
| 13 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the Scheduling Data Source |
| 14 | `DATA_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Data Source Code |
| 15 | `DISPLAY_ID` | DOUBLE | NOT NULL |  | Display Identifier |
| 16 | `DISPLAY_MEANING` | VARCHAR(12) |  |  | Display Meaning |
| 17 | `DISPLAY_TABLE` | VARCHAR(32) |  |  | Display Table |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 20 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 21 | `PARENT_MEANING` | VARCHAR(12) |  |  | Parent Meaning |
| 22 | `PARENT_TABLE` | VARCHAR(32) |  |  | Parent Table |
| 23 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

