# DASH_COMPONENT

> Dashboard Component Table

**Description:** DASHBOARD COMPONENT  
**Table type:** REFERENCE  
**Primary key:** `DASH_COMPONENT_ID`  
**Columns:** 24  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMPONENT_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Component. |
| 7 | `COMPONENT_TEMPLATE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Component Template. |
| 8 | `CONTENT_DATA_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Long_Text_Reference table containing this Component's content data. |
| 9 | `DASH_COMPONENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 10 | `DASH_DASHBOARD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Dashboard Table. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | person last updating the dashboard component |
| 13 | `MINI_WIKI_TXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Long_Text_Reference table containing this Component's mini wiki text. |
| 14 | `ORG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Organization table. |
| 15 | `ORIG_DASH_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | Reference to Original Component Record. Required for Versioning |
| 16 | `RECOMMENDED_DIMENSIONS_TXT` | VARCHAR(20) |  |  | The recommended dimensions for this Component. |
| 17 | `SAMPLE_DATA_TXT` | VARCHAR(2000) |  |  | The sample data to be used for rendering the Component in the Config Tool. |
| 18 | `SHIPPED_IND` | DOUBLE | NOT NULL |  | True if shipped from Cerner. |
| 19 | `TEMPLATE_IND` | DOUBLE | NOT NULL |  | True if record represents a Template Component. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_DATA_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `DASH_DASHBOARD_ID` | [DASH_DASHBOARD](DASH_DASHBOARD.md) | `DASH_DASHBOARD_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MINI_WIKI_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIG_DASH_COMPONENT_ID` | [DASH_COMPONENT](DASH_COMPONENT.md) | `DASH_COMPONENT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DASH_COMPONENT](DASH_COMPONENT.md) | `ORIG_DASH_COMPONENT_ID` |
| [DASH_COMPONENT_SETTING](DASH_COMPONENT_SETTING.md) | `DASH_COMPONENT_ID` |
| [DASH_TYPE_COMPONENT_RELTN](DASH_TYPE_COMPONENT_RELTN.md) | `DASH_COMPONENT_ID` |

