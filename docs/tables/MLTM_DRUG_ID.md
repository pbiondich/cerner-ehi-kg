# MLTM_DRUG_ID

> This table contains a listing of all of Multum's unique generic drug identifiers, as well as specific attributes of each.

**Description:** This table contains a listing of all of Multum's unique generic drug identifiers  
**Table type:** REFERENCE  
**Primary key:** `DRUG_IDENTIFIER`  
**Columns:** 12  
**Referenced by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | PK | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". |
| 2 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique numeric identifier for a description of a drug. |
| 3 | `EMPIRICALLY` | VARCHAR(1) |  |  | This field indicates whether drug half-life information is available for the drug. |
| 4 | `HALF_LIFE` | DOUBLE |  |  | This field contains an estimate of the amount of time necessary for a drug to be eliminated from the body. This estimate may be used to determine the length of time to continue checking for a drug interaction after use of a drug is discontinued. The length of time is reported as a half-life measured in hours. |
| 5 | `IS_SINGLE_INGREDIENT` | VARCHAR(1) |  |  | This field indicates whether a drug is available as a single product or if it is only available in combination with other drugs. |
| 6 | `MAX_THERAPEUTIC_DUPLICATION` | DOUBLE |  |  | This field contains a number representing how many orders for a specified drug may be prescribed before therapeutic duplication warnings should be generated. |
| 7 | `PREGNANCY_ABBR` | VARCHAR(1) |  |  | This is a one-character field that represents the FDA's pregnancy hazard classification scheme. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_SYNONYM_ID` | [MLTM_DRUG_NAME](MLTM_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |

## Referenced by (14)

| From table | Column |
|------------|--------|
| [MLTM_ADDITIONAL_TEXT](MLTM_ADDITIONAL_TEXT.md) | `DRUG_IDENTIFIER` |
| [MLTM_ALR_CATEGORY_DRUG_MAP](MLTM_ALR_CATEGORY_DRUG_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_CATEGORY_DRUG_XREF](MLTM_CATEGORY_DRUG_XREF.md) | `DRUG_IDENTIFIER` |
| [MLTM_DRUG_LEAFLET_MAP](MLTM_DRUG_LEAFLET_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_DRUG_MODIFIER_MAP](MLTM_DRUG_MODIFIER_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_DUPLICATION_DRUG_XREF](MLTM_DUPLICATION_DRUG_XREF.md) | `DRUG_IDENTIFIER` |
| [MLTM_FTD_TEXT](MLTM_FTD_TEXT.md) | `DRUG_IDENTIFIER` |
| [MLTM_FTD_TEXT_CONDITION](MLTM_FTD_TEXT_CONDITION.md) | `DRUG_IDENTIFIER` |
| [MLTM_INT_DRUG_INTERACTIONS](MLTM_INT_DRUG_INTERACTIONS.md) | `DRUG_IDENTIFIER_1` |
| [MLTM_INT_DRUG_INTERACTIONS](MLTM_INT_DRUG_INTERACTIONS.md) | `DRUG_IDENTIFIER_2` |
| [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `DRUG_IDENTIFIER` |
| [MLTM_REF_DRUG](MLTM_REF_DRUG.md) | `DRUG_IDENTIFIER` |
| [MLTM_XP_CLIN_TEXT_XREF](MLTM_XP_CLIN_TEXT_XREF.md) | `DRUG_IDENTIFIER` |
| [PBS_OCS_MAPPING](PBS_OCS_MAPPING.md) | `DRUG_IDENTIFIER` |

