# CHART_LAW_FILTER_VALUE

> This table stores the details for each cross-encounter law. (DistributionTool.exe)

**Description:** This table stores the details for each cross-encounter law.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DESCRIPTION` | VARCHAR(60) | NOT NULL |  | The parent_entity_name description of the parent_entity_id. |
| 6 | `KEY_SEQUENCE` | DOUBLE | NOT NULL |  | makes unique row |
| 7 | `LAW_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the cross-encounter law. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The detail Identifier for the cross-encounter law. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent_entity table. |
| 10 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | This is relationship type (code_value). |
| 11 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Type Flag: 0=Encounter Type, 1=Organization, 2=Provider, 3=Location, 4=Medical Service |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAW_ID` | [CHART_LAW](CHART_LAW.md) | `LAW_ID` |

