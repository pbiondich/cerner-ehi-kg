# MLLD_RXN_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXN_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The Multum drug synonym id |
| 2 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Multum main drug code |
| 3 | `RXCUI` | VARCHAR(60) | NOT NULL |  | Identifier from RxNorm terminology. |
| 4 | `RXN_DESCRIPTION` | VARCHAR(3000) |  |  | The descriptor for the RxNorm translation |
| 5 | `TERM_TYPE_MEANING` | VARCHAR(20) | NOT NULL |  | Defines the type of term |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_SYNONYM_ID` | [MLLD_DRUG_NAME](MLLD_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |

