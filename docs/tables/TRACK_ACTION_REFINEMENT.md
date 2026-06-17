# TRACK_ACTION_REFINEMENT

> Describes how a tracking action will be launched.

**Description:** Track Action Refinement  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key from the parent table identified in PARENT_ENTITY_NAME - this is replicated from TRACK_ACTION to support RDDS merge delete. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entitythis is replicated from TRACK_ACTION to support RDDS merge delete for parent/child tables. |
| 3 | `REFINEMENT_CONTENT` | VARCHAR(256) | NOT NULL |  | Refinement value data. Describes a custom field. |
| 4 | `REFINEMENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary Key from a parent table identified in REFINEMENT_ENTITY_NAME. (TRACK_EVENT, TRACK_PREFERENCE, CODE_VALUE, DCP_FORMS_REF) |
| 5 | `REFINEMENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the parent entity for REFINEMENT_ENTITY_ID(TRACK_EVENT, TRACK_PREFERENCE, CODE_VALUE, DCP_FORMS_REF) |
| 6 | `REFINEMENT_NAME` | VARCHAR(64) | NOT NULL |  | Describes the data being held in this refinement |
| 7 | `TRACK_ACTION_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY ID from the TRACK ACTION table for the action that these refinements are describing |
| 8 | `TRACK_ACTION_REFINEMENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_ACTION_ID` | [TRACK_ACTION](TRACK_ACTION.md) | `TRACK_ACTION_ID` |

