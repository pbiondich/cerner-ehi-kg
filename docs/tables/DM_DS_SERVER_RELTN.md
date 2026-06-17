# DM_DS_SERVER_RELTN

> This is a Relationship table for the DM_DS_SERVER, DM_DS_SERVICE, and DM_DS_TEMPLATE tables.

**Description:** DM_DS_SERVER_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_DS_SERVER_ID` | DOUBLE | NOT NULL | FK→ | SERVER IDENTIFIER |
| 2 | `DM_DS_SERVER_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `DM_DS_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | SERVICE IDENTIFIER |
| 4 | `DM_DS_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | TEMPLATE IDENTIFIER |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_DS_SERVER_ID` | [DM_DS_SERVER](DM_DS_SERVER.md) | `DM_DS_SERVER_ID` |
| `DM_DS_SERVICE_ID` | [DM_DS_SERVICE](DM_DS_SERVICE.md) | `DM_DS_SERVICE_ID` |
| `DM_DS_TEMPLATE_ID` | [DM_DS_TEMPLATE](DM_DS_TEMPLATE.md) | `DM_DS_TEMPLATE_ID` |

