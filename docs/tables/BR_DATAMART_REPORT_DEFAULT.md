# BR_DATAMART_REPORT_DEFAULT

> Stores default data at the report level for the setup of mpages in the bedrock wizard

**Description:** BR_DATAMART_REPORT_DEFAULT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_REPORT_DEFAULT_ID` | DOUBLE | NOT NULL |  | Unique id for the row |
| 2 | `BR_DATAMART_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Id from br_datamart_report table |
| 3 | `MPAGE_PARAM_MEAN` | VARCHAR(25) | NOT NULL |  | Unique meaning for an Mpage setup parameter |
| 4 | `MPAGE_PARAM_VALUE` | VARCHAR(255) | NOT NULL |  | Default value for an Mpage setup parameter |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_REPORT_ID` | [BR_DATAMART_REPORT](BR_DATAMART_REPORT.md) | `BR_DATAMART_REPORT_ID` |

