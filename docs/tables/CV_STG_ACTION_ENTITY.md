# CV_STG_ACTION_ENTITY

> This table holds the details of the actions taken by personnel/entities for respective staged documents.

**Description:** Cardiovascular Staging Action Entity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | ACTION DATE TIME |
| 2 | `ACTION_ORG_ID` | DOUBLE |  |  | Millennium identifier of the ORGANIZATION that took the specified action. The constraint has been dropped because the column could contain external data. We have a mechanism in our service to validate the Ids before we post any data to patient chart. If any invalid values found we want to continue to stage the data which is posting in this table. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE |  |  | Millennium identifier of the personnel who took the specified action. The constraint has been dropped because the column could contain external data. We have a mechanism in our service to validate the Ids before we post any data to patient chart. If any invalid values found we want to continue to stage the data which is posting in this table. |
| 4 | `ACTION_TYPE_CD` | DOUBLE |  |  | Code value to represent the tpye of action.; |
| 5 | `ACTION_TZ` | DOUBLE |  |  | ACTION TZ |
| 6 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `CV_STG_ACTION_ENTITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `CV_STG_METADATA_ID` | DOUBLE |  | FK→ | The staging metadata identifier.; |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TZ` | DOUBLE |  |  | UPDT TIME ZONE |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_STG_METADATA_ID` | [CV_STG_METADATA](CV_STG_METADATA.md) | `CV_STG_METADATA_ID` |

