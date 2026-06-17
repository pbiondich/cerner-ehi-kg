# CHART_DIST_FILTER_VALUE

> chart distribution filter value

**Description:** This table defines the values included or excluded for each selection criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DESCRIPTION` | VARCHAR(60) |  |  | The description of the data that is defined to be included or exclude for a particular selection criteria |
| 6 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | The id uniquely defined for the chart distribution |
| 7 | `KEY_SEQUENCE` | DOUBLE | NOT NULL |  | Provides the ability to define multiple filters per distribution and selection criteria |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the code for the data that is being included or excluded for the selection criteria. The code set that this code comes from varies based onthe selection criteria. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Contains the name of the table to which value of parent_entity_id fields belongs |
| 10 | `QUALIFIER` | VARCHAR(10) |  |  | not used at this time |
| 11 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | This field coupled with the type_flag = 2 and parent_entity_id field shows the relationship type chosen with that particular provider. |
| 12 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | This defines the type of criteria that will be included or excluded from a distribution |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |

