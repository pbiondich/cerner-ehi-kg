# MLLD_NDC_INNER_CORE_DESC

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_NDC_INNER_CORE_DESC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_CODE` | DOUBLE | NOT NULL |  | This field contains a unique code for each brand name. |
| 2 | `GBO` | VARCHAR(1) | NOT NULL |  | This field designates the product's status as a brand name product or a generic product. This status is based on Multum's internal editorial rules and cost algorithms that are used to determine whether a multi-source drug is generic or not. |
| 3 | `INNER_NDC_CODE` | VARCHAR(25) | NOT NULL |  | The National Drug Code is the standard 11-digit identifier for each drug product, as recognized by HCFA, other federal and state agencies, and many commercial enterprises. It is unique to each specific product. The first 5 numbers identify the manufacturer of a product. The second 4 numbers identify the product, and the last 2 numbers identify the package size of that product. |
| 4 | `INNER_PACKAGE_DESC_CODE` | DOUBLE | NOT NULL |  | This field contains a code that represents units that describe the package size. Not all drug products require a package unit description for a complete representation of the packaging. |
| 5 | `INNER_SIZE` | DOUBLE | NOT NULL |  | This field represents the number of individual units present in the innermost packaging of a drug. |
| 6 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. |
| 7 | `NDC_FORMATTED` | VARCHAR(25) | NOT NULL |  | This field presents the National Drug Code in the format #####-####-##, where the first set of numbers identify the manufacturer of a product, the second set of numbers identify the product, and the last set identifies the package size of the product. This field differs from the ndc_code field in that it includes dashes between each set of numbers. |
| 8 | `OBSOLETE_DATE` | DATETIME |  |  | This field contains data only if a drug product is no longer being manufactured. It will contain the date when the product became obsolete. Multum uses the shelf expiration date of the last batch produced by a manufacturer, or the date of drug withdrawal, when available. When not available, Multum provides its best estimate of the obsolete date based on information provided by wholesalers and manufacturers. |
| 9 | `ORANGE_BOOK_ID` | DOUBLE | NOT NULL |  | This field contains a unique code for each Orange Book code. |
| 10 | `OTC_STATUS` | VARCHAR(1) | NOT NULL |  | This field designates whether a product is available by prescription only (Rx) or if it is available over-the-counter (OTC). |
| 11 | `OUTER_PACKAGE_SIZE` | DOUBLE | NOT NULL |  | This field designates the total number of inner packages present in the final packaged product. Not all drug products require an outer package size for a complete representation of the packaging. (The package unit may suffice.) |
| 12 | `REPACKAGED` | VARCHAR(1) | NOT NULL |  | This field indicates whether another drug vendor has repackaged the original product. |
| 13 | `SOURCE_ID` | DOUBLE | NOT NULL |  | This field contains a unique code for each drug source (manufacturer/redistributor). |
| 14 | `UNIT_DOSE_CODE` | VARCHAR(1) | NOT NULL |  | This one character designation indicates if the product is supplied in unit dose packaging. Valid choices are: U - Packaged in unit dose. N - Not packaged in unit dose. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

