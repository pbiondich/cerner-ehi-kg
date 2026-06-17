# OEN_SCRIPT_HIST

> History table for holding oen_script row revisions

**Description:** OEN SCRIPT HISTORY  
**Table type:** REFERENCE  
**Primary key:** `OEN_SCRIPT_HIST_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUILD_DT_TM` | DATETIME |  |  | Date time with seconds precision for when the script was built in the domain |
| 2 | `NOT_EXECUTABLE_IND` | DOUBLE |  |  | An Indicator which determines if script is executable by user or not. |
| 3 | `OEN_SCRIPT_HIST_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY - A unique generated number that identifies a unique row |
| 4 | `READ_ONLY_IND` | DOUBLE |  |  | AN Indicator which determines if a script is read only or not. |
| 5 | `SCRIPT_DESC` | VARCHAR(80) |  |  | Description of the script version |
| 6 | `SCRIPT_NAME` | CHAR(32) | NOT NULL | FK→ | Script name of the unique parent row in oen_script table |
| 7 | `SCRIPT_REFCNT` | DOUBLE | NOT NULL |  | Historical revision count of the script |
| 8 | `SCRIPT_TYPE` | VARCHAR(20) |  |  | Type of the script (need examples) |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `USER_NAME` | VARCHAR(32) |  |  | User name of the user who created the revision |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRIPT_NAME` | [OEN_SCRIPT](OEN_SCRIPT.md) | `SCRIPT_NAME` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OEN_SCRIPT_HIST_CLOB](OEN_SCRIPT_HIST_CLOB.md) | `OEN_SCRIPT_HIST_ID` |

