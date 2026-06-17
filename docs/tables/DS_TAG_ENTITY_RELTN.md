# DS_TAG_ENTITY_RELTN

> Associates providers from Millennium PRSNL or HPD_PROVIDER to DS_TAG

**Description:** Directory Search Tag Provider Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DS_TAG_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `DS_TAG_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the DS_TAG table |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is a soft Foreign Key value from either the Millennium PRSNL table, or from the HPD_PROVIDER table. The related table is identifie in the PARENT_ENTITY_NAME field. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the table ( PRSNL / HPD_PROVIDER) from which the PARENT_ENTITY_ID value comes from. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DS_TAG_ID` | [DS_TAG](DS_TAG.md) | `DS_TAG_ID` |

