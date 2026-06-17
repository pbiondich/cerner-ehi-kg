# BR_ADO_ORD_LIST

> Stores Synonyms and associated Sentences for Options under a Facility, Topic, Scenario and Category.

**Description:** Bedrock Advisor Orders Order Lists  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The detail this Order List pertains to. Foreign Key to BR_ADO_DETAIL Table. |
| 2 | `BR_ADO_OPTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies Options. Foreign Key to BR_ADO_OPTION |
| 3 | `BR_ADO_ORD_LIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_ADO_ORD_LIST table. |
| 4 | `SENTENCE_ID` | DOUBLE | NOT NULL |  | Identifies Sentences for synonyms. |
| 5 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Identifies Synonyms under Options. |
| 6 | `SYNONYM_SEQ` | DOUBLE | NOT NULL |  | Value to sequence the synonyms configured to an option. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_DETAIL_ID` | [BR_ADO_DETAIL](BR_ADO_DETAIL.md) | `BR_ADO_DETAIL_ID` |
| `BR_ADO_OPTION_ID` | [BR_ADO_OPTION](BR_ADO_OPTION.md) | `BR_ADO_OPTION_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

