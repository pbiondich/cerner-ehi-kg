# DM_DS_TEMPLATE

> Store information about Database Service Templates

**Description:** DM_DS_TEMPLATE  
**Table type:** REFERENCE  
**Primary key:** `DM_DS_TEMPLATE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_DS_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | The Template Identifier |
| 2 | `TEMPLATE_DESCRIPTION` | VARCHAR(80) | NOT NULL |  | Template Description |
| 3 | `TEMPLATE_NAME` | VARCHAR(30) | NOT NULL |  | Template Name |
| 4 | `TEMPLATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Template Type. 1 = Cerner, 2 = Client |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_DS_SERVER_RELTN](DM_DS_SERVER_RELTN.md) | `DM_DS_TEMPLATE_ID` |

