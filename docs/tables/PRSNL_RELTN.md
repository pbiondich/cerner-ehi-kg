# PRSNL_RELTN

> This table contains demographic, address, and phone relationships for personnel

**Description:** PRSNL RELTN  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_RELTN_ID`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Sequence used by the application to display relationships |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the prsnl_reltn row is related (i.e., organization_id) |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table to which this prsnl_reltn row is related (i.e., ORGANIZATION) |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `PRSNL_RELTN_ID` | DOUBLE | NOT NULL | PK | The primary key of the Prsnl_Reltn table |
| 12 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of relationship (i.e., Demographic, Address, Phone) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `PRSNL_RELTN_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `PRSNL_RELTN_ID` |
| [EPRESCRIBE_DETAIL](EPRESCRIBE_DETAIL.md) | `PRSNL_RELTN_ID` |
| [PRSNL_RELTN_ACTIVITY](PRSNL_RELTN_ACTIVITY.md) | `PRSNL_RELTN_ID` |
| [PRSNL_RELTN_CHILD](PRSNL_RELTN_CHILD.md) | `PRSNL_RELTN_ID` |

