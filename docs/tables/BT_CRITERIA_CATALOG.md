# BT_CRITERIA_CATALOG

> Bill Template Criteria Catalog

**Description:** Bill Template Criteria Catalog  
**Table type:** REFERENCE  
**Primary key:** `BT_CRITERIA_CAT_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_CLASS_CD` | DOUBLE | NOT NULL |  | Bill Class Code |
| 7 | `BT_CRITERIA_CAT_ID` | DOUBLE | NOT NULL | PK | Bill Template Criteria Catalog ID |
| 8 | `CODE_SET` | DOUBLE |  |  | Code Set |
| 9 | `CONTROL_NBR` | DOUBLE |  |  | Control Number |
| 10 | `CRITERIA_DESC` | VARCHAR(250) |  |  | Criteria Description |
| 11 | `CRITERIA_NAME` | VARCHAR(250) |  |  | Criteria Name |
| 12 | `CRITERIA_NAME_KEY` | VARCHAR(250) |  |  | Criteria Name Key |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `BT_CRITERIA_CAT_ID` |
| [BT_COND_CRIT_RELTN](BT_COND_CRIT_RELTN.md) | `BT_CRITERIA_CAT_ID` |

