# PIE_DWL_LIST

> This table will store the list of all the lists associated to the current user.

**Description:** Dynamic Worklists  
**Table type:** ACTIVITY  
**Primary key:** `PIE_DWL_LIST_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `LIST_NAME` | VARCHAR(50) | NOT NULL |  | Specified name for the list created by the user. |
| 3 | `PIE_DWL_LIST_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the pie_dwl_list table. Each change or revision made creates a new instance within the group. The first instance id (PK value) is used for the group ID. |
| 4 | `PIE_DWL_LIST_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `USER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID of the personnel who created the list. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PIE_DWL_LIST_GROUP_ID` | [PIE_DWL_LIST](PIE_DWL_LIST.md) | `PIE_DWL_LIST_ID` |
| `USER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PIE_DWL_LIST](PIE_DWL_LIST.md) | `PIE_DWL_LIST_GROUP_ID` |
| [PIE_DWL_LIST_PERSON_R](PIE_DWL_LIST_PERSON_R.md) | `PIE_DWL_LIST_ID` |

