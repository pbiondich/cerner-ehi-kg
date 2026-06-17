# MLTM_NDC_MAIN_DRUG_CODE

> Contains a listing of all MMDCs - an important link to ancillary tables. Each MMDC contains a unique combination of the following: drug_identifier, principal_route_code, dose_form_code, and product_strength_code.

**Description:** Contains a listing of all MMDCs - an important link to ancillary tables  
**Table type:** REFERENCE  
**Primary key:** `MAIN_MULTUM_DRUG_CODE`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSA_SCHEDULE` | VARCHAR(2) |  |  | This field describes the drug class assigned to a specific product type (MMDC) under the Controlled Substances Act of 1970. |
| 2 | `DOSE_FORM_CKI` | VARCHAR(255) |  |  | CKI Code |
| 3 | `DOSE_FORM_CODE` | DOUBLE |  | FK→ | This field contains a numeric designation for a dose form. |
| 4 | `DRUG_IDENTIFIER` | VARCHAR(6) |  | FK→ | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". |
| 5 | `GLOBAL_SECONDARY_IDENT` | VARCHAR(50) |  |  | Global drug identifier |
| 6 | `GLOBAL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the type of Global Identifier stored in Global Secondary Id |
| 7 | `J_CODE` | VARCHAR(10) |  |  | This is Multum's designation for the Health Care Common Procedure Code (J-Code) used for submitting claims to insurance organizations. |
| 8 | `J_CODE_DESCRIPTION` | VARCHAR(50) |  |  | This field contains the full text of the Health Care Common Procedures Billing Code Description, including the code itself, the reimbursable route of administration, and the amount of drug to be administered. |
| 9 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL | PK | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. |
| 10 | `PRINCIPAL_ROUTE_CKI` | VARCHAR(255) |  |  | CKI code |
| 11 | `PRINCIPAL_ROUTE_CODE` | DOUBLE |  |  | This field contains a code for the principal (or most common) route of administration for a specific drug (MMDC). Values for these codes are located in the Multum_product_route table. |
| 12 | `PRODUCT_STRENGTH_CODE` | DOUBLE |  | FK→ | This field contains a unique code for each product strength description. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOSE_FORM_CODE` | [MLTM_DOSE_FORM](MLTM_DOSE_FORM.md) | `DOSE_FORM_CODE` |
| `DRUG_IDENTIFIER` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `GLOBAL_TYPE_ID` | [MLTM_GLOBAL_TYPE](MLTM_GLOBAL_TYPE.md) | `GLOBAL_TYPE_ID` |
| `PRODUCT_STRENGTH_CODE` | [MLTM_PRODUCT_STRENGTH](MLTM_PRODUCT_STRENGTH.md) | `PRODUCT_STRENGTH_CODE` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [MLTM_DDM_GROUP_MMDC_MAP](MLTM_DDM_GROUP_MMDC_MAP.md) | `MAIN_MULTUM_DRUG_CODE` |
| [MLTM_DRC_GROUP_RELTN](MLTM_DRC_GROUP_RELTN.md) | `MAIN_MULTUM_DRUG_CODE` |
| [MLTM_MMDC_ATTRIBUTE](MLTM_MMDC_ATTRIBUTE.md) | `MAIN_MULTUM_DRUG_CODE` |
| [MLTM_RXB_ORDER](MLTM_RXB_ORDER.md) | `MAIN_MULTUM_DRUG_CODE` |
| [PBS_OCS_MAPPING](PBS_OCS_MAPPING.md) | `MAIN_MULTUM_DRUG_CODE` |

