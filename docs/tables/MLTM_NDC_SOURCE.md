# MLTM_NDC_SOURCE

> This table contains a listing of all the drug sources (manufacturers, redistributors, and repackagers) whose products occur in the ndc_core_description table. It also includes addresses for each source.

**Description:** Contains a listing of all the drug sources which occur in ndc_core_description.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS1` | VARCHAR(100) |  |  | This field contains line 1 of the street addresses for the manufacturers/redistributors of drug products. |
| 2 | `ADDRESS2` | VARCHAR(100) |  |  | This field contains line 2 of the street address for the manufacturers/redistributors of drug products. |
| 3 | `CITY` | VARCHAR(50) |  |  | This field contains the names of the cities where manufacturers/redistributors are located. |
| 4 | `COUNTRY` | VARCHAR(50) |  |  | This field contains the names of the countries where manufacturers/repackagers are located. |
| 5 | `PROVINCE` | VARCHAR(30) |  |  | This field identifies the provinces of the countries in which manufacturers/redistributors are located, if applicable. |
| 6 | `SOURCE_DESC` | VARCHAR(120) |  |  | This field contains the names of manufacturers, redistributor, and repackagers of drug products. |
| 7 | `SOURCE_ID` | DOUBLE | NOT NULL |  | This field contains a unique code for each drug source (manufacturer/redistributor). |
| 8 | `STATE` | VARCHAR(30) |  |  | This field contains a unique code for each drug source (manufacturer/redistributor). |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `ZIP` | VARCHAR(10) |  |  | This field contains the 10-character zip codes of manufacturers/redistributors. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

