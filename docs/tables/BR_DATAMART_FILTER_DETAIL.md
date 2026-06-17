# BR_DATAMART_FILTER_DETAIL

> stores additional data for a filter

**Description:** Bedrock Datamart Filter Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_FILTER_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique ID for the table |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | FK→ | unique_id from br_datamart_filter table |
| 3 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | unique meaning from oe_field_meaning table |
| 4 | `REQUIRED_IND` | DOUBLE |  |  | indicates optional or required for the detail |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_FILTER_ID` | [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_FILTER_ID` |

