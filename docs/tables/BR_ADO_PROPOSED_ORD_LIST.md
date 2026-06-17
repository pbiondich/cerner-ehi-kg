# BR_ADO_PROPOSED_ORD_LIST

> Stores Proposed Synonyms and associated Sentence for Proposed Options under Topic, Scenario and Category.

**Description:** Bedrock Advisor Orders Proposed Order Lists  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_PROPOSED_OPTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Option this order list pertains to. Foreign Key to BR_ADO_PROPOSED_OPTION |
| 2 | `BR_ADO_PROPOSED_ORD_LIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_ADO_PROPOSED_ORD_LIST table. |
| 3 | `PROPOSED_SENTENCE_TXT` | VARCHAR(255) |  |  | Contains Proposed Sentence Information |
| 4 | `SYNONYM_NAME` | VARCHAR(100) | NOT NULL |  | Identifies Synonyms under Options. |
| 5 | `SYNONYM_SEQ` | DOUBLE | NOT NULL |  | Value to sequence the synonyms configured to an option. |
| 6 | `SYNONYM_UNIQUE_IDENT` | VARCHAR(255) | NOT NULL |  | identifies Synonym. Can contain CKI or Concept CKI of the Synonym |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_PROPOSED_OPTION_ID` | [BR_ADO_PROPOSED_OPTION](BR_ADO_PROPOSED_OPTION.md) | `BR_ADO_PROPOSED_OPTION_ID` |

