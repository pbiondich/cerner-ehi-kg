# DCP_FORMS_ACTIVITY_COMP

> List all of the components for a given activity form

**Description:** Components of Forms Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_CD` | DOUBLE | NOT NULL |  | Type of component |
| 2 | `DCP_FORMS_ACTIVITY_COMP_ID` | DOUBLE | NOT NULL |  | Unique, generated key for DCP_FORMS_ACTIVITY_COMP. |
| 3 | `DCP_FORMS_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Activity form component is part of |
| 4 | `DESCRIPTION` | VARCHAR(100) |  |  | textual description |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of parent entity. This corresponds to the component_cd |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of parent entity |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_FORMS_ACTIVITY_ID` | [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `DCP_FORMS_ACTIVITY_ID` |

