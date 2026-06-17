# NOMENCLATURE_OUTBOUND

> This table is used to translate a nomenclature_id to a source identifier of another source vocabulary for outbound interfaces.

**Description:** Nomenclature Outbound  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS` | VARCHAR(255) | NOT NULL |  | The outbound alias to the nomenclature_id. |
| 2 | `ALIAS_TYPE_MEANING` | VARCHAR(255) |  |  | The meaning of the alias. Used when alias is not unique enough within a source vocabulary. |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number |
| 4 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The external vocabulary or lexicon that the nomenclature_id is being aliased. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

