# STRT_ASSAY

> Cerner-owned information about assays that will be used to facilitate database building and maintenance for medical device interfaces

**Description:** Starter assay  
**Table type:** REFERENCE  
**Primary key:** `STRT_ASSAY_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSAY_TYPE` | DOUBLE |  |  | Used to store the assay type for a specific starter assay. Valid types are 1-Chemistry, 2-Coagulation, 3-Hematology, 4-immunology/Serology, 5-Cytopathology, 6-Therapeutic Monitoring/Toxicology/Drugs, 7-Microbiology, 8-Urinalysis, 99- All |
| 2 | `DESCRIPTION` | VARCHAR(100) |  |  | Used to store the Cerner-owned description for the assay |
| 3 | `MNEMONIC` | VARCHAR(100) |  |  | Used to store the abbreviated description for the assay |
| 4 | `STRT_ASSAY_CD` | DOUBLE | NOT NULL |  | This value is used to standardize Assay information across systems. |
| 5 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL | PK | RDBMS assigned unique key field. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `STRT_ASSAY_ID` |
| [STRT_MODEL_ASSAY_ALIAS](STRT_MODEL_ASSAY_ALIAS.md) | `STRT_ASSAY_ID` |

