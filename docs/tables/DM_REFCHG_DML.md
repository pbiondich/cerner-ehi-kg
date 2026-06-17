# DM_REFCHG_DML

> Data management reference change DML cutover overrides to use when cutting over in RDDS.

**Description:** Data Management Reference Change DML  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the column (if applicable) needing the override. |
| 2 | `DATA_TYPE` | VARCHAR(30) | NOT NULL |  | Contains the data type of the attribute. Valid values are Char, Number, or Date. |
| 3 | `DML_ATTRIBUTE` | VARCHAR(100) | NOT NULL |  | Contains the attribute to override. For example: upd_val_str, versioning_ind, etc. |
| 4 | `DML_VALUE` | VARCHAR(255) | NOT NULL |  | The value to which the attribute is to be set. |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table needing the override. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

