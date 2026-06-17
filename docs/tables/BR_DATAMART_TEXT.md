# BR_DATAMART_TEXT

> table to store text for categories/reports/filter

**Description:** Bedrock Datamart Text  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | id from br_datamart_category |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Id from br_datamart_filter_id |
| 3 | `BR_DATAMART_REPORT_ID` | DOUBLE | NOT NULL |  | Report ID from BR_datamart_report table |
| 4 | `BR_DATAMART_TEXT_ID` | DOUBLE | NOT NULL |  | unique id for text |
| 5 | `TEXT_SEQ` | DOUBLE |  |  | sequence to display text for categories,reports, and filters |
| 6 | `TEXT_TYPE_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for type of text |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `BR_DATAMART_FILTER_ID` | [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_FILTER_ID` |

