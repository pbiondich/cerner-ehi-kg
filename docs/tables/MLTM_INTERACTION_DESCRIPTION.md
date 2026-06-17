# MLTM_INTERACTION_DESCRIPTION

> This table provides a textual description of each interaction and a unique code for each description. Specifically, the descriptions discuss the nature of the interaction, the frequency of occurrence (when known), the mechanism of action (when known), and a recommendation for appropriate clinical action.

**Description:** Multum Interaction Description  
**Table type:** REFERENCE  
**Primary key:** `INT_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INT_DESCRIPTION` | VARCHAR(2000) |  |  | ** Obsolete ** This column is no longer used. Will be replaced by new column INT_DESC_TEXT. |
| 2 | `INT_DESC_TEXT` | LONGTEXT |  |  | Long Textual description of each interaction. |
| 3 | `INT_ID` | DOUBLE | NOT NULL | PK | a unique code for each description. Primary Key. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLTM_INT_DRUG_INTERACTIONS](MLTM_INT_DRUG_INTERACTIONS.md) | `INT_ID` |
| [MLTM_INT_INTERACT_SEVERITY_MAP](MLTM_INT_INTERACT_SEVERITY_MAP.md) | `INT_ID` |

