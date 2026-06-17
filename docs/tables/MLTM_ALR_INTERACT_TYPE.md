# MLTM_ALR_INTERACT_TYPE

> This table contains the interaction_type_id that is necessary for displaying appropriate messages to end users. It also contains a textual description of each allergic interaction type for purposes of application development only.

**Description:** Multum allergy interaction type  
**Table type:** REFERENCE  
**Primary key:** `INTERACTION_TYPE_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERACTION_DESCRIPTION` | VARCHAR(255) |  |  | a textual description of each allergic interaction type for purposes of application development only. |
| 2 | `INTERACTION_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary Key. Necessary for displaying appropriate messages to end users. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_ALR_TEXT_MAP](MLTM_ALR_TEXT_MAP.md) | `INTERACTION_TYPE_ID` |

