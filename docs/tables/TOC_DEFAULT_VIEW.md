# TOC_DEFAULT_VIEW

> The table defines the default chart view per TOC (Table of Content) filter per user within PowerChart and clones

**Description:** TOC DEFAULT VIEW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Solution Specific Application Number |
| 2 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The order in which the tab will display |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID for the User - FK value from the PERSON_ID on the PRSNL table. |
| 4 | `TOC_DEFAULT_VIEW_ID` | DOUBLE | NOT NULL |  | Primary Key - a unique generated number that identifies a unique row on the table |
| 5 | `TOC_FILTER_CD` | DOUBLE | NOT NULL |  | TOC (Table of Content) Filters from code set 4001984 |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEW_CAPTION` | VARCHAR(256) | NOT NULL |  | The display name of the tab, as it is seen in PowerChart and clones. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

