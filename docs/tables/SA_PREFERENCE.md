# SA_PREFERENCE

> Parent record for a subset of preference values used for anesthesia preferences Based on how many different views they want to have. Estimate < 100 rows initially - but may grow as users become more familiar with system. 100

**Description:** SA Preference  
**Table type:** REFERENCE  
**Primary key:** `SA_PREFERENCE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location that this preference group is valid for, any location if 0 |
| 6 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | The procedure that this preference group is valid for, any procedure if 0 |
| 7 | `POSITION_CD` | DOUBLE | NOT NULL |  | Stores position code that this preference applies to |
| 8 | `PREFERENCE_SET_NAME` | CHAR(50) |  |  | The display name of the preference group for this record |
| 9 | `PREFERENCE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Defines the type of preference group this record is |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user that has access to this preference group, any user if 0 |
| 11 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (i.e., Anesthesia, Case Tracking, CVNet - CardioVascular). |
| 12 | `SA_PREFERENCE_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the preference group |
| 13 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Doc Type that the Preference Set is tied to |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFERENCE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_REF_DOC_TYPE_ID` | [SA_REF_DOC_TYPE](SA_REF_DOC_TYPE.md) | `SA_REF_DOC_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_PREFERENCE_VALUE](SA_PREFERENCE_VALUE.md) | `SA_PREFERENCE_ID` |

