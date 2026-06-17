# BR_ORDSENT_DETAIL

> Stores the individual fields of an order sentence

**Description:** Bedrock Order Sentence Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ORDSENT_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique ID for the table |
| 2 | `BR_ORDSENT_ID` | DOUBLE | NOT NULL | FK→ | Value from the BR_ORDSENT table. |
| 3 | `OE_FIELD_MEANING` | VARCHAR(255) | NOT NULL |  | order entry field meaning |
| 4 | `OE_FIELD_VALUE` | VARCHAR(255) | NOT NULL |  | value for the order entry field |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ORDSENT_ID` | [BR_ORDSENT](BR_ORDSENT.md) | `BR_ORDSENT_ID` |

