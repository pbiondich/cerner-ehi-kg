# BR_SCH_TEMP_SLOT_RELEASE_R

> Stores the release slots associated to the template slots.

**Description:** Bedrock Scheduling Template Release Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_SCH_TEMP_SLOT_RELEASE_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_SCH_TEMP_SLOT_RELEASE_R table. |
| 2 | `BR_SCH_TEMP_SLOT_R_ID` | DOUBLE | NOT NULL | FK→ | The slot that is available for release. |
| 3 | `RELEASE_END_TIME_STR` | VARCHAR(40) | NOT NULL |  | Stores when the release will end. |
| 4 | `RELEASE_NAME` | VARCHAR(100) | NOT NULL |  | Stores the name of the release. |
| 5 | `RELEASE_START_TIME_STR` | VARCHAR(40) | NOT NULL |  | Stores when the release will start. |
| 6 | `RELEASE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The slot type that can be released. |
| 7 | `RELEASE_UNIT` | VARCHAR(10) | NOT NULL |  | Stores the release unit. |
| 8 | `RELEASE_UNIT_VALUE_STR` | VARCHAR(10) | NOT NULL |  | Stores the release unit value. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_SCH_TEMP_SLOT_R_ID` | [BR_SCH_TEMP_SLOT_R](BR_SCH_TEMP_SLOT_R.md) | `BR_SCH_TEMP_SLOT_R_ID` |
| `RELEASE_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |

