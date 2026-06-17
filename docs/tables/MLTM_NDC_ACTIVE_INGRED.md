# MLTM_NDC_ACTIVE_INGRED

> This table provides the full salt/chemical name of all active ingredients of drug products available in the United States

**Description:** Multum NDC Active Ingredients  
**Table type:** REFERENCE  
**Primary key:** `ACTIVE_INGREDIENT_CODE`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_INGREDIENT_CODE` | DOUBLE | NOT NULL | PK | This field contains a unique code for each active ingredient |
| 2 | `ACTIVE_INGREDIENT_TXT` | VARCHAR(255) | NOT NULL |  | This field contains textual descriptions of active drug ingredients; it contains complete salt/chemical/ester names and is therefore ideally suited for many applications desighed for pharmacist end users. In general, the drug_name field, may be more appropriate for use in applications designed for clinical or consumer end users. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_NDC_ACT_INGRED_LIST](MLTM_NDC_ACT_INGRED_LIST.md) | `ACTIVE_INGREDIENT_CODE` |

