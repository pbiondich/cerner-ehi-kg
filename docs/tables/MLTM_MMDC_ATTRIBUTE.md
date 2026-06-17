# MLTM_MMDC_ATTRIBUTE

> This table contains attributes about a Multum Formulation (MMDC - main multum drug code) which are derived from other Multum tables.

**Description:** Multum MMDC Attribute  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVAILABLE_IND` | DOUBLE |  |  | Indicates the drug is currently being marketed |
| 2 | `GENERIC_FORM_IND` | DOUBLE |  |  | Indicates if drug has a generic form. |
| 3 | `GENERIC_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Contains synonym ID for generic name |
| 4 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL | FK→ | Unique ID - from the Main Multum Drug Code Table |
| 5 | `OTC_STATUS` | DOUBLE |  |  | Status of drug availability Over The Counter |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GENERIC_SYNONYM_ID` | [MLTM_DRUG_NAME](MLTM_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| `MAIN_MULTUM_DRUG_CODE` | [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `MAIN_MULTUM_DRUG_CODE` |

