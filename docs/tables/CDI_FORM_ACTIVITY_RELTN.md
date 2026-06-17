# CDI_FORM_ACTIVITY_RELTN

> A row in this table represents a relationship between a form activity and another identifier, such as the relationship between a queued ABN form and rows on the EEM_ABN_CHECK table.

**Description:** CDI Form Activity Reltn  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CDI_FORM_ACTIVTY table. |
| 2 | `CDI_FORM_ACTIVITY_RELTN_ID` | DOUBLE | NOT NULL |  | The unique primary key of the CDI_FORM_ACTIVTY_RELTN table. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the parent table row associated to the form activity. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table associated to the form activity. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_ACTIVITY_ID` | [CDI_FORM_ACTIVITY](CDI_FORM_ACTIVITY.md) | `CDI_FORM_ACTIVITY_ID` |

