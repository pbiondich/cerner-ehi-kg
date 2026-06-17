# SN_SUPPLY_CAB_DEF_PREFS

> Stores the segments and event code defaults for supply cabinet information.

**Description:** SN Supply Cabinet Default Preferences  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type for which a list of segments and event codes will display |
| 2 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code of the field |
| 3 | `SEG_CD` | DOUBLE | NOT NULL |  | For this document type, the segment on which supply cabinet data will default |
| 4 | `SN_SUPPLY_CAB_DEF_PREFS_ID` | DOUBLE | NOT NULL |  | primary key |
| 5 | `SUP_CAB_DATA_ELM_CD` | DOUBLE | NOT NULL |  | Code of the supply cabinet data element |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

