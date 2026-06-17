# BR_DATAMART_DEFAULT_DETAIL

> Stores additional data for a default result

**Description:** Bedrock Datamart Default Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_DEFAULT_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique ID for the table. |
| 2 | `BR_DATAMART_DEFAULT_ID` | DOUBLE | NOT NULL | FK→ | Unique ID from the BR_DATAMART_DEFAULT table |
| 3 | `DETAIL_CKI` | VARCHAR(255) | NOT NULL |  | cki value for default detail |
| 4 | `DETAIL_VALUE` | VARCHAR(255) | NOT NULL |  | free text value for the default detail |
| 5 | `OE_FIELD_MEANING` | VARCHAR(25) | NOT NULL |  | unique meaning from oe_field_meaning table |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_DEFAULT_ID` | [BR_DATAMART_DEFAULT](BR_DATAMART_DEFAULT.md) | `BR_DATAMART_DEFAULT_ID` |

