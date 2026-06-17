# OSM_FORM_CLIENT_VALUES

> Table used to store the Id's of the actual information used on the Form.

**Description:** OSM FORM CLIENT VALUES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Unique field id for different types of fields specific to form |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Organization Location code_value |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization Id for specific client value |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of record from the Parent_Entity_Name |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Name of Table where Parent_Entity_Id is found |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORM_FIELD_ID` | [OSM_FORM_FIELDS](OSM_FORM_FIELDS.md) | `FORM_FIELD_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

