# CMN_IMPORT_ACTIVITY

> Activity table for tracking the import activities of configuration management entities

**Description:** Configuration Management Import Activity  
**Table type:** ACTIVITY  
**Primary key:** `CMN_IMPORT_ACTIVITY_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMN_IMPORT_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `CMN_IMPORT_TYPE` | VARCHAR(15) |  |  | The type of Import eg Mpage or views |
| 3 | `IMPORT_DT_TM` | DATETIME |  |  | DATE AND TIME OF THE IMPORT |
| 4 | `PERFORMING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user ID that performed the activity |
| 5 | `PROCESS_GUID` | VARCHAR(50) | NOT NULL |  | GUID for identifying a batch import operation |
| 6 | `REPLACEMENT_NAME` | VARCHAR(150) |  |  | The replacement of the imported or swapped Entity |
| 7 | `REPL_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID VALUE ASSOCIATED TO THE PK OF THE TABLE IDENTIFIED IN COLUMN REPLACEMENT_PARENT_ENTITY_NAME |
| 8 | `REPL_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table from which an ID value is used for REPL_PARENT_ENTITY_ID - either BR_DATAMART_CATEGORY or MP_VIEWPOINT |
| 9 | `REQUESTED_NAME` | VARCHAR(150) |  |  | The requested name of the imported or swapped Entity |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERFORMING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CMN_NAME_SWAP_ACTIVITY](CMN_NAME_SWAP_ACTIVITY.md) | `CMN_IMPORT_ACTIVITY_ID` |

