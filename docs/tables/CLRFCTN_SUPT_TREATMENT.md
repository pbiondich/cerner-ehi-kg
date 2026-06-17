# CLRFCTN_SUPT_TREATMENT

> Treatments that support the clarification

**Description:** CLRFCTN_SUPT_TREATMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLARIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Identifier for row on the Clarification Table |
| 2 | `CLRFCTN_SUPT_TREATMENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CLARIFICATION_SUPT_TREATMENT table. |
| 3 | `TREATMENT_CLASS` | VARCHAR(128) |  |  | Supporting treatment class |
| 4 | `TREATMENT_DISPLAY` | VARCHAR(128) |  |  | Supporting treatment display |
| 5 | `UPDATED_IND` | DOUBLE | NOT NULL |  | UPDATED? 1 = yes 0 = no |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLARIFICATION_ID` | [CLARIFICATION](CLARIFICATION.md) | `CLARIFICATION_ID` |

