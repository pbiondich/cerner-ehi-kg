# OSM_FORM_GROUP_VALUES

> Table used to store id's of actual information for given forms.

**Description:** OSM FORM GROUP VALUES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Unique Id for different types of fields specific to a form |
| 2 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique Id for a Form Group |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique Id for the actual information for the form that comes from the Parent_Entity_Name table |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Table where Parent_Entity_Name belongs |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORM_FIELD_ID` | [OSM_FORM_FIELDS](OSM_FORM_FIELDS.md) | `FORM_FIELD_ID` |
| `GROUP_ID` | [OSM_FORM_GROUPS](OSM_FORM_GROUPS.md) | `GROUP_ID` |

