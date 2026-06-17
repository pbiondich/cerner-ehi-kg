# MLLD_MED_GUIDE_LINK

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_MED_GUIDE_LINK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The Brand Level Description of the NDC specified |
| 2 | `BRAND_DESCRIPTION_IDENT` | VARCHAR(25) | NOT NULL |  | The Drug Synonym ID for the Brand Level entry for the NDC specified |
| 3 | `BRAND_FUNCTION_ID` | DOUBLE | NOT NULL |  | The Multum assigned function id for the ndc specified |
| 4 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | Multum's identifier for generic drugs |
| 5 | `GENERIC_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The description of the generic form of the NDC specified. |
| 6 | `GENERIC_DESCRIPTION_IDENT` | VARCHAR(25) | NOT NULL |  | The Drug Synonym ID for the Generic form of the NDC specified. |
| 7 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | High-Level identifier used by Multum to denote similar drugs |
| 8 | `MEDGUIDE_LINK` | VARCHAR(255) | NOT NULL |  | URL which points to the medical guide for the given NDC. |
| 9 | `NDC_CODE` | VARCHAR(25) | NOT NULL |  | The FDA assigned National Drug Code for a drug |
| 10 | `PRIMARY_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The Primary level description of the NDC specified |
| 11 | `PRIMARY_DESCRIPTION_IDENT` | VARCHAR(25) | NOT NULL |  | The Drug Synonym ID for the Primary Level entry for the NDC specified |
| 12 | `TRADE_DESCRIPTION` | VARCHAR(255) |  |  | The description of the trade form of the NDC specified |
| 13 | `TRADE_DESCRIPTION_IDENT` | VARCHAR(25) |  |  | The Drug Synonym ID for the Trade form of the NDC specified |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

