# BR_VOCABULARY

> Reference data will be stored on this table. The data will assist in proposing new vocabulary to be loaded by bedrock.

**Description:** Bedrock Vocabulary  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_VOCABULARY_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table. |
| 2 | `SOURCE_IDENTIFIER` | VARCHAR(50) |  |  | The code or key from the vocabulary that contributed the string. |
| 3 | `SOURCE_NAME` | VARCHAR(40) |  |  | The name of the vocabulary's source. |
| 4 | `SOURCE_STRING` | VARCHAR(255) |  |  | Variable length string contributed by the source vocabulary. |
| 5 | `SOURCE_VOCAB_MEAN` | VARCHAR(12) |  |  | The meaning of the vocabulary that contributed the string. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

