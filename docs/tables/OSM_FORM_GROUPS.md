# OSM_FORM_GROUPS

> Table used to store specific grouping id's for Forms

**Description:** OSM FORM GROUPS  
**Table type:** REFERENCE  
**Primary key:** `GROUP_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_DESCRIPTION` | VARCHAR(100) |  |  | Name or description of group |
| 2 | `GROUP_ID` | DOUBLE | NOT NULL | PK | Unique Id for grouping for Form |
| 3 | `OSM_FORM_ID` | DOUBLE | NOT NULL | FK→ | Unique Form identifier |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OSM_FORM_ID` | [OSM_FORM](OSM_FORM.md) | `OSM_FORM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OSM_FORM_GROUP_VALUES](OSM_FORM_GROUP_VALUES.md) | `GROUP_ID` |
| [OSM_FORM_ORG_GRP_XREF](OSM_FORM_ORG_GRP_XREF.md) | `GROUP_ID` |

