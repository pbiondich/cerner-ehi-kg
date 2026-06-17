# MLLD_DRUG_ID

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DRUG_ID  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". |
| 2 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | This field contains a unique numeric identifier for a description of a drug. |
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

