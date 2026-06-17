# LH_D_CQM_RXNORM_MAP

> This table is used to store reference data based off of the Clinical Quality Measures Bedrock and Multum components

**Description:** LH_D_RXNORM_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMOUNT_NBR` | DOUBLE | NOT NULL |  | The Amount of the drug |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The Millennium catalog code for the order |
| 4 | `CATEGORY_MEAN` | VARCHAR(100) |  |  | Unique string for a category |
| 5 | `DOSE_CD` | DOUBLE | NOT NULL |  | The Millennium code value for the dosage of the medication |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 8 | `GENERIC_DRUG_NAME_TXT` | VARCHAR(255) |  |  | The generic name of the drug from Multum |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 10 | `LH_D_CQM_RXNORM_MAP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_CQM_RXNORM_MAP table. |
| 11 | `MLTM_ACTIVE_INGRED_TXT` | VARCHAR(255) |  |  | The Multum code value for the primary route of the RxNorm |
| 12 | `MLTM_DOSE_ABBR_TXT` | VARCHAR(50) |  |  | The Multum abbreviation for the dosage of the RxNorm |
| 13 | `MLTM_DOSE_CODE` | DOUBLE | NOT NULL |  | The Multum code value for the primary route of the RxNorm |
| 14 | `MLTM_DOSE_DESC_TXT` | VARCHAR(255) |  |  | The Multum description for the dosage of the RxNorm |
| 15 | `MLTM_DRUG_IDENT_TXT` | VARCHAR(255) |  |  | The Multum code value for the primary route of the RxNorm |
| 16 | `MLTM_ROUTE_ABBR_TXT` | VARCHAR(50) |  |  | The Multum abbreviation for the route of the RxNorm |
| 17 | `MLTM_ROUTE_CODE` | DOUBLE | NOT NULL |  | The Multum code value for the primary route of the RxNorm |
| 18 | `MLTM_ROUTE_DESC_TXT` | VARCHAR(50) |  |  | The Multum description for the route of the RxNorm |
| 19 | `MLTM_UNIT_ABBR_TXT` | VARCHAR(255) |  |  | The Multum code value for the primary route of the RxNorm |
| 20 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 21 | `ROUTE_CD` | DOUBLE | NOT NULL |  | The Millennium code value for the route of the drug |
| 22 | `RXNORM_TXT` | VARCHAR(25) |  |  | The RxNorm |
| 23 | `UNIT_CD` | DOUBLE | NOT NULL |  | The Millennium code value for the units of the medication |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record |
| 27 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VALUE_SET_NAME` | VARCHAR(255) |  |  | Unique string for a value set identifier |
| 29 | `VOCAB_OID_TXT` | VARCHAR(100) |  |  | The the CMS defined OID for the Value Set |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

