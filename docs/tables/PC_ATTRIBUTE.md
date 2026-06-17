# PC_ATTRIBUTE

> This table is a reference table for PC attributes. It will hold all PC attributes.

**Description:** PC Attribute  
**Table type:** REFERENCE  
**Primary key:** `ATTRIBUTE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIBUTE_DESC` | VARCHAR(500) |  |  | The PC attribute description |
| 3 | `ATTRIBUTE_DISPLAY_NAME` | VARCHAR(256) |  |  | The PC attribute display name |
| 4 | `ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | Primary Key; Unique number identifying the PC attribute |
| 5 | `ATTRIBUTE_LOC_NAME` | VARCHAR(100) | NOT NULL |  | The PC attribute location path name |
| 6 | `ATTRIBUTE_LOC_PATH` | VARCHAR(256) | NOT NULL |  | The PC attribute location path |
| 7 | `ATTRIBUTE_NAME` | VARCHAR(50) | NOT NULL |  | The PC attribute name |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PC_ATTRIBUTE_VALUE](PC_ATTRIBUTE_VALUE.md) | `ATTRIBUTE_ID` |

