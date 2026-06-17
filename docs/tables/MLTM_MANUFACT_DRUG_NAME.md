# MLTM_MANUFACT_DRUG_NAME

> Table used to store the manufacture ordered drug name for combination drugs.

**Description:** MLTM_MANUFACT_DRUG_NAME  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Table used to store the manufacture ordered drug name for combination drugs. |
| 2 | `IS_OBSOLETE` | VARCHAR(1) | NOT NULL |  | Determines whether the drug name has been made obsolete |
| 3 | `MANUFACTURER_ORDERED_DRUG_NAME` | VARCHAR(255) | NOT NULL |  | Stores the manufacture ordered drug name for combination drugs |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_SYNONYM_ID` | [MLTM_DRUG_NAME](MLTM_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |

