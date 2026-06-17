# MLLD_DRUG_NAME

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DRUG_NAME  
**Table type:** REFERENCE  
**Primary key:** `DRUG_SYNONYM_ID`  
**Columns:** 8  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_NAME` | VARCHAR(255) |  |  | This field contains Multum's succinct, fixed-length generic drug names. This field also contains brand names, which are the drug names as they appear on labels of drug products. |
| 2 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | PK | This field contains a unique numeric identifier for a description of a drug. |
| 3 | `IS_OBSOLETE` | VARCHAR(1) |  |  | This field indicates whether a drug is currently available on the market in the United States. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MLLD_DMD_NAME_MAP](MLLD_DMD_NAME_MAP.md) | `DRUG_SYNONYM_ID` |
| [MLLD_DRUG_NAME_GLOBAL_TYPE](MLLD_DRUG_NAME_GLOBAL_TYPE.md) | `DRUG_SYNONYM_ID` |
| [MLLD_MANUFACT_DRUG_NAME](MLLD_MANUFACT_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| [MLLD_RXN_MAP](MLLD_RXN_MAP.md) | `DRUG_SYNONYM_ID` |

