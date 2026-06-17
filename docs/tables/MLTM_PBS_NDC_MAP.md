# MLTM_PBS_NDC_MAP

> Table used to store mappings between PBS codes and NDC Codes

**Description:** MLTM PBS NDC MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_NAME` | VARCHAR(45) | NOT NULL |  | Brand Name associated to record |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | Multum Drug Identifier |
| 3 | `DRUG_NAME` | VARCHAR(255) | NOT NULL |  | Drug Name associated to record |
| 4 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | Multum defined code. |
| 5 | `MANUFACTURER_CODE` | VARCHAR(20) | NOT NULL |  | MANUFACTURER CODE FROM TABLE PBS_MANUFACTURER |
| 6 | `MULTUM_MEDICAL_SUPPLY_CODE` | DOUBLE | NOT NULL |  | Medical Supply code defined by Multum |
| 7 | `NDC_CODE` | VARCHAR(25) | NOT NULL |  | NDC Code as defined by Multum |
| 8 | `PACK_SIZE` | DOUBLE | NOT NULL |  | QUANTITY CONTAINED IN MANUFACTURER'S PACKAGE |
| 9 | `PBS_ITEM_CODE` | VARCHAR(5) | NOT NULL |  | PBS_CODE defined by external source. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

