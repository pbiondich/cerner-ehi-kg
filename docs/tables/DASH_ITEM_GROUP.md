# DASH_ITEM_GROUP

> Dashboard Item Groups Table

**Description:** DASHBOARD ITEM GROUPS  
**Table type:** REFERENCE  
**Primary key:** `DASH_ITEM_GROUP_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTENT_DATA_TXT` | VARCHAR(1000) | NOT NULL |  | The Content of the Item Group |
| 6 | `DASH_DASHBOARD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Dashboard Table. |
| 7 | `DASH_ITEM_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `GROUP_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Group. |
| 9 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person last updating the item group |
| 10 | `ORG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Organization table. |
| 11 | `SHIPPED_IND` | DOUBLE | NOT NULL |  | True if shipped from Cerner. |
| 12 | `TEMPLATE_IND` | DOUBLE | NOT NULL |  | True if record represents a Template Dashboard. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DASH_DASHBOARD_ID` | [DASH_DASHBOARD](DASH_DASHBOARD.md) | `DASH_DASHBOARD_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DASH_FILTER](DASH_FILTER.md) | `DASH_ITEM_GROUP_ID` |

