# CNT_WV_ITEM_DTA

> Contains details about working view item and display association DTA details, which are used by Bedrock tool. Imported using content manager tool.

**Description:** Working view item - display association dta relation table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_WV_ITEM_DTA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | UID of the DTA which is part of display association. Value comes from field in CNT_DTA_KEY2 |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WV_ITEM_UID` | VARCHAR(100) | NOT NULL |  | Working view item UIDWorking view item UID for which DTA's associated as display association.value from CNT_WV_ITEM_KEY table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

