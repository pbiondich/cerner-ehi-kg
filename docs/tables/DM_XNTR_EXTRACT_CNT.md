# DM_XNTR_EXTRACT_CNT

> Stores information about the row counts retrieve for each extract file

**Description:** Database Architecture Extract and Tranform Retrieve Extract Count  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELETED_ROW_CNT` | DOUBLE |  |  | Holds the number of rows deleted from the Live table in case of an error |
| 2 | `DM_XNTR_EXTRACT_CNT_ID` | DOUBLE | NOT NULL |  | Non-intelligent PK of table |
| 3 | `DM_XNTR_EXTRACT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to DM_XNTR_EXTRACT table, which holds pointer to each extract for a given job |
| 4 | `RETRIEVED_ROW_CNT` | DOUBLE |  |  | Holds the number of rows inserted back into the live table |
| 5 | `TABLE_NAME` | VARCHAR(30) |  |  | Holds the table name of the data retrieved |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_XNTR_EXTRACT_ID` | [DM_XNTR_EXTRACT](DM_XNTR_EXTRACT.md) | `DM_XNTR_EXTRACT_ID` |

