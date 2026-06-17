# DM_PURGE_TEMPLATE

> HNAM purge job template information.

**Description:** DM PURGE TEMPLATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FEATURE_NBR` | DOUBLE | NOT NULL |  | Rev Tool Feature number to which this purge template was promoted. |
| 3 | `NAME` | VARCHAR(255) |  |  | Name of the purge template. This will be displayed to the client. |
| 4 | `PROGRAM_STR` | VARCHAR(255) |  |  | Name of CCL program which needs to be run to get the top-level table's rowids. |
| 5 | `SCHEMA_DT_TM` | DATETIME |  |  | Date/time this purge template modification was promoted in Feature Tracker. |
| 6 | `TEMPLATE_NBR` | DOUBLE | NOT NULL |  | Number (id) of the purge template that this job uses. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

