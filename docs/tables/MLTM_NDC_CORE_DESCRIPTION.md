# MLTM_NDC_CORE_DESCRIPTION

> Contains a listing of information about specific NDC-labeled products including the manufacturer, packaging information, and over-the-counter/prescription-only status. It also contains the MMDC to link each NDC to "higher-level" information in Multum DB.

**Description:** Contains a listing of information about specific NDC-labeled products.  
**Table type:** REFERENCE  
**Primary key:** `NDC_CODE`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_CODE` | DOUBLE |  |  | This field contains a unique code for each brand name. |
| 2 | `GBO` | VARCHAR(1) |  |  | This field designates the product's status as a brand name product or a generic product. This status is based on Multum's internal editorial rules and cost algorithms that are used to determine whether a multi-source drug is generic or not. |
| 3 | `GLOBAL_SECONDARY_IDENT` | VARCHAR(50) | NOT NULL |  | Global drug identifier |
| 4 | `GLOBAL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the type of Global Identifier stored in Global Secondary Id (from MLTM_GLOBAL_TYPE) |
| 5 | `INNER_PACKAGE_DESC_CODE` | DOUBLE |  |  | This field contains a code that represents units that describe the package size. Not all drug products require a package unit description for a complete representation of the packaging. |
| 6 | `INNER_PACKAGE_SIZE` | DOUBLE |  |  | This field represents the number of individual units present in the innermost packaging of a drug. |
| 7 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE |  |  | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. |
| 8 | `NDC_CODE` | VARCHAR(25) | NOT NULL | PK | The National Drug Code is the standard 11-digit identifier for each drug product, as recognized by HCFA, other federal and state agencies, and many commercial enterprises. It is unique to each specific product. The first 5 numbers identify the manufacturer of a product. The second 4 numbers identify the product, and the last 2 numbers identify the package size of that product. |
| 9 | `NDC_FORMATTED` | VARCHAR(25) | NOT NULL |  | This field presents the National Drug Code in the format #####-####-##, where the first set of numbers identify the manufacturer of a product, the second set of numbers identify the product, and the last set identifies the package size of the product. This field differs from the ndc_code field in that it includes dashes between each set of numbers. |
| 10 | `NDC_REGULATION` | VARCHAR(10) |  |  | National Drug Code RegulationColumn |
| 11 | `NDC_SCHEME` | VARCHAR(3) |  |  | National Drug Code SchemeColumn |
| 12 | `OBSOLETE_DATE` | DATETIME |  |  | This field contains data only if a drug product is no longer being manufactured. It will contain the date when the product became obsolete. Multum uses the shelf expiration date of the last batch produced by a manufacturer, or the date of drug withdrawal, when available. When not available, Multum provides its best estimate of the obsolete date based on information provided by wholesalers and manufacturers. |
| 13 | `ORANGE_BOOK_ID` | DOUBLE | NOT NULL |  | This field contains a unique code for each Orange Book code. |
| 14 | `OTC_STATUS` | VARCHAR(1) |  |  | This field designates whether a product is available by prescription only (Rx) or if it is available over-the-counter (OTC). |
| 15 | `OUTER_PACKAGE_SIZE` | DOUBLE |  |  | This field designates the total number of inner packages present in the final packaged product. Not all drug products require an outer package size for a complete representation of the packaging. (The package unit may suffice.) |
| 16 | `REPACKAGED` | VARCHAR(1) |  |  | This field indicates whether another drug vendor has repackaged the original product. |
| 17 | `SOURCE_ID` | DOUBLE | NOT NULL |  | This field contains a unique code for each drug source (manufacturer/redistributor). |
| 18 | `UNIT_DOSE_CODE` | VARCHAR(1) |  |  | This one character designation indicates if the product is supplied in unit dose packaging. Valid choices are: U - Packaged in unit dose. N - Not packaged in unit dose. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GLOBAL_TYPE_ID` | [MLTM_GLOBAL_TYPE](MLTM_GLOBAL_TYPE.md) | `GLOBAL_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_NDC_COST](MLTM_NDC_COST.md) | `NDC_CODE` |

