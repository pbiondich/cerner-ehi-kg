# CODE_VALUE_MODS

> Stores references to codes changed on the code_value table

**Description:** CODE_VALUE CHANGES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI` | VARCHAR(255) |  |  | Reference to the CKI identifier on the CODE_VALUE table which experienced a change (INSERT/UPDATE) |
| 2 | `CODE_SET` | DOUBLE | NOT NULL |  | Reference to the CODE_SET value identifier on the CODE_VALUE table which experienced a change (INSERT/UPDATE) |
| 3 | `CODE_VALUE` | DOUBLE | NOT NULL |  | Reference to the code value identifier on the CODE_VALUE table which experienced a change (INSERT/UPDATE) |
| 4 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Reference to the CONCEPT CKI identifier on the CODE_VALUE table which experienced a change (INSERT/UPDATE) |
| 5 | `LOGICAL_CNT` | DOUBLE | NOT NULL |  | Alternate Key of the table, used as a logical counter of changes added. It is assumed that each new addition has a value greater than any other identifier on the table. |
| 6 | `LOGICAL_CNT_INDEX` | DOUBLE | NOT NULL |  | PRIMARY KEY. will populate the column manually using a trigger. We will use this new column to create a simple window of changes. The new column will be calculated using a formula similar to "LOGICAL_CNT MOD x", where x is the size of the window. As a simple example, say we declare x to be 10, meaning we will keep at most 10 items on the table. Once the 11th change is reported, we will go back and overwrite the 1st item. This new column will help us limit the number of rows in the table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

