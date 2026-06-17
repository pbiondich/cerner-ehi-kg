# CHART_SERVER_PRINTER

> A current listing of all the front end printers installed on the chart servers.

**Description:** Chart Server Printers  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_SERVER_PRINTER_ID` | DOUBLE | NOT NULL |  | Primary Key. Value from CHART_VIEW_SEQ |
| 2 | `CS_PARAM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to chart server settings table |
| 3 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Ouitput_dest_cd installed on chart server. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CS_PARAM_ID` | [CHART_SERVER_SETTINGS](CHART_SERVER_SETTINGS.md) | `CS_PARAM_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |

