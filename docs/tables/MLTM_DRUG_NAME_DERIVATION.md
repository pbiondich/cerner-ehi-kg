# MLTM_DRUG_NAME_DERIVATION

> This table contains the mapping of generic and trade names to their respective generic product and trade product names. Only generic or trade names that have an associated MMDC will have generic or trade product names.

**Description:** Used to find and display available dosage forms and routes for a given name.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | This field contains the drug synonym ID of the generic or trade name used to generate a particular generic or trade product name. |
| 2 | `BASE_FUNCTION_ID` | DOUBLE | NOT NULL |  | This field contains the function ID (generic or trade) of the base_drug_synonym_id. |
| 3 | `DERIVED_DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | This field contains the drug synonym ID of the generic or trade product name that was derived from a generic or trade name combined with a Main Multum Drug Code (MMDC). |
| 4 | `DERIVED_FUNCTION_ID` | DOUBLE | NOT NULL |  | This field contains the function ID (59 or 60) of the derived_drug_synonym_id. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

