# DASH_TYPE

> Identifies the Dashboard Type and assigns a unique Name

**Description:** DASHBOARD TYPE  
**Table type:** REFERENCE  
**Primary key:** `DASH_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DASH_TYPE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `DASH_TYPE_NAME` | VARCHAR(100) | NOT NULL |  | Name of the Dashboard Type |
| 4 | `ORG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Organization table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DASH_DASHBOARD](DASH_DASHBOARD.md) | `DASH_TYPE_ID` |
| [DASH_TYPE_COMPONENT_RELTN](DASH_TYPE_COMPONENT_RELTN.md) | `DASH_TYPE_ID` |

