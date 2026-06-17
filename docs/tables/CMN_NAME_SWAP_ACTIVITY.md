# CMN_NAME_SWAP_ACTIVITY

> Activity table for tracking the name swap activities of configuration management entities

**Description:** Configuration Management Name Swap Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMN_IMPORT_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier in CMN_IMPORT_ACTIVITY table used as a parent ID for Name swap activity. |
| 2 | `CMN_NAME_SWAP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `NAME_SWAP_DT_TM` | DATETIME |  |  | The date and time the name swap was done |
| 4 | `PERFORMING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The User ID that performed the activity |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CMN_IMPORT_ACTIVITY_ID` | [CMN_IMPORT_ACTIVITY](CMN_IMPORT_ACTIVITY.md) | `CMN_IMPORT_ACTIVITY_ID` |
| `PERFORMING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

