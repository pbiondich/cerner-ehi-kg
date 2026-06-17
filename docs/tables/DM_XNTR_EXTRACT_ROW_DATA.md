# DM_XNTR_EXTRACT_ROW_DATA

> Stores rowids for eachextract that was retrieved using the XnTR process

**Description:** Database Architecture Extract and Transform - Retrive Extract Row Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_XNTR_EXTRACT_ROW_DATA_ID` | DOUBLE | NOT NULL |  | Non-intelligent PK of table |
| 2 | `EXTRACT_ID` | DOUBLE | NOT NULL |  | Foreign Key to DM_XNTR_EXTRACT.DM_XNTR_EXTRACT_ID |
| 3 | `NEW_ROWID` | VARCHAR(10) |  |  | Holds the rowid of the row that was inserted into the table |
| 4 | `TABLE_NAME` | VARCHAR(100) | NOT NULL |  | Holds the table_name of the row that was inserted |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

