# DM_REFCHG_ATTRIBUTE

> This table will store additional metadata for reference tables that will be used by RDDS

**Description:** DM_REFCHG_ATTRIBUTE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_CHAR` | VARCHAR(2000) |  |  | Contains value of character attributes |
| 2 | `ATTRIBUTE_DT_TM` | DATETIME |  |  | Contains value of date attributes |
| 3 | `ATTRIBUTE_NAME` | VARCHAR(50) | NOT NULL |  | Contains meta-data attribute |
| 4 | `ATTRIBUTE_VALUE` | DOUBLE |  |  | Contains value of numeric attributes |
| 5 | `COLUMN_NAME` | VARCHAR(30) |  |  | Column name the attribute is associated with |
| 6 | `DM_REFCHG_ATTRIBUTE_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 7 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Table name the attribute is associated with |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

