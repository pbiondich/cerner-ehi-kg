# DASH_FILTER

> The Dashboard Filter table

**Description:** DASHBOARD FILTERS  
**Table type:** REFERENCE  
**Primary key:** `DASH_FILTER_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTENT_DATA_TXT` | VARCHAR(1000) | NOT NULL |  | The Content of the Filter. |
| 7 | `DASH_DASHBOARD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Dashboard Table. |
| 8 | `DASH_FILTER_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `DASH_ITEM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Dash_Item_Group Table. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FILTER_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Filter. |
| 12 | `FILTER_TEMPLATE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Filter Template. |
| 13 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | person last updating the dashboard filter |
| 14 | `ORG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Organization table. |
| 15 | `ORIG_DASH_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Reference to Original Filter Record. Required for Versioning |
| 16 | `SHIPPED_IND` | DOUBLE | NOT NULL |  | True if shipped from Cerner. |
| 17 | `TEMPLATE_IND` | DOUBLE | NOT NULL |  | True if record represents a Template Filter. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DASH_DASHBOARD_ID` | [DASH_DASHBOARD](DASH_DASHBOARD.md) | `DASH_DASHBOARD_ID` |
| `DASH_ITEM_GROUP_ID` | [DASH_ITEM_GROUP](DASH_ITEM_GROUP.md) | `DASH_ITEM_GROUP_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIG_DASH_FILTER_ID` | [DASH_FILTER](DASH_FILTER.md) | `DASH_FILTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DASH_FILTER](DASH_FILTER.md) | `ORIG_DASH_FILTER_ID` |

