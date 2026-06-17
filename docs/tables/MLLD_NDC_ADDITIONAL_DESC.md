# MLLD_NDC_ADDITIONAL_DESC

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_NDC_ADDITIONAL_DESC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EQUIVALENT_BRAND_ID` | DOUBLE | NOT NULL |  | This field contains an identifier representing equivalent brand names for a particular product. |
| 2 | `NDC_LEFT_9` | VARCHAR(9) | NOT NULL |  | This field presents the National Drug Code that is unique to a product, the left 9 characters without the remaining 2, which are packaging descriptions. |
| 3 | `TOP_200_IND` | DOUBLE |  |  | This field designates a drug's status as one of the 200 most prescribed brand or generic drugs in the United States during the previous year. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

