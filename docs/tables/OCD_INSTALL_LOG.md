# OCD_INSTALL_LOG

> Log table for tracking of components installed via OCD.

**Description:** OCD INSTALL LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_TYPE` | VARCHAR(40) | NOT NULL |  | Component type. |
| 2 | `END_STATE` | VARCHAR(40) | NOT NULL |  | End state name or number. |
| 3 | `INSTALL_DT_TM` | DATETIME | NOT NULL |  | Date and time of the installation. |
| 4 | `INSTALL_TEXT` | VARCHAR(1000) |  |  | Stores free text information related to package installation. |
| 5 | `LOG_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 6 | `OCD` | DOUBLE | NOT NULL |  | OCD containing the component. |
| 7 | `UPDATE_IND` | DOUBLE | NOT NULL |  | Update indicator (for future use). |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

