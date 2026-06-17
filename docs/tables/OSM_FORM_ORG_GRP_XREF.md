# OSM_FORM_ORG_GRP_XREF

> Cross Reference table for the Group and Form Table

**Description:** OSM FORM ORG GRP XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique Group Identifier |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Organization Location identifier |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique Organization Id |
| 4 | `OSM_FORM_ID` | DOUBLE | NOT NULL | FK→ | Unique Form Specific Id |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ID` | [OSM_FORM_GROUPS](OSM_FORM_GROUPS.md) | `GROUP_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OSM_FORM_ID` | [OSM_FORM](OSM_FORM.md) | `OSM_FORM_ID` |

