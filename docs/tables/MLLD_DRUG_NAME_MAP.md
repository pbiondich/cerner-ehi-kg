# MLLD_DRUG_NAME_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DRUG_NAME_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". |
| 2 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | This field contains a unique numeric identifier for a description of a drug. |
| 3 | `FUNCTION_ID` | DOUBLE | NOT NULL |  | This field contains a numeric identifier that describes the classification of an entry. For example, a function_id of 16 represents a generic name for a drug; a function_id of 5 represents pregnancy text. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

