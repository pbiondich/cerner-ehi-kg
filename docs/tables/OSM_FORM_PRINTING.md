# OSM_FORM_PRINTING

> Contains records of forms that an user can print.

**Description:** OSM FORM PRINTING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_PRINT_DT_TM` | DATETIME |  |  | Last date and time form was printed |
| 2 | `LAST_PRINT_NUMBER` | DOUBLE | NOT NULL |  | Last number from requisition bucket to be printed. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Organization Location code_value |
| 4 | `NUMBER_COPIES` | DOUBLE | NOT NULL |  | Number of forms that was last printed. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization Id for specific form |
| 6 | `OSM_FORM_ID` | DOUBLE | NOT NULL | FK→ | Unique Id for a form |
| 7 | `PRINT_IND` | DOUBLE | NOT NULL |  | Print Indicator for running operation jobs |
| 8 | `THRESHOLD` | DOUBLE | NOT NULL |  | How low requisition numbers will go before new forms will be printed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OSM_FORM_ID` | [OSM_FORM](OSM_FORM.md) | `OSM_FORM_ID` |

