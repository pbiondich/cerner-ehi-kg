# BR_DATAMART_REPORT_FILTER_R

> Relationships between datamart reports and filters.

**Description:** Bedrock Datamart Report Filter R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | FK→ | ID from BR_DATAMART_FILTER table |
| 2 | `BR_DATAMART_REPORT_FILTER_R_ID` | DOUBLE | NOT NULL |  | Unique ID for each row of the table |
| 3 | `BR_DATAMART_REPORT_ID` | DOUBLE | NOT NULL |  | Value from the BR_datamart_report table |
| 4 | `DENOMINATOR_IND` | DOUBLE | NOT NULL |  | Indicates the type of filter |
| 5 | `NUMERATOR_IND` | DOUBLE | NOT NULL |  | Indicates the type of filter |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_FILTER_ID` | [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_FILTER_ID` |

