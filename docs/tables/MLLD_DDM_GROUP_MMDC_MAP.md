# MLLD_DDM_GROUP_MMDC_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DDM_GROUP_MMDC_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_ID` | DOUBLE | NOT NULL |  | Group ID - 1st column in 2-column PK. FK From MLTM_DDM_GROUP table. |
| 2 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | Main Multum Drug Code. 2nd column in 2-column PK. FK from MLTM_NDC_MAIN_DRUG_CODE table |
| 3 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL |  | Multum Category ID - FK from MLTM_DRUG_CATEGORIES table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

