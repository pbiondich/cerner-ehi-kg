# PCS_HIERARCHY

> Stores the hierarchies used for Clinical Validation. A hierarchy consists of assigned queues in a specific order (referred to as levels). Clinical results are routed to a hierarchy. Once in approved in the first queue, they are sent to each subsequent queue until fully approved.

**Description:** Stores the hierarchies used for Clinical Validation.  
**Table type:** REFERENCE  
**Primary key:** `HIERARCHY_ID`  
**Columns:** 17  
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
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `HIERARCHY_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the hierarchy. |
| 8 | `HIERARCHY_NAME` | VARCHAR(100) | NOT NULL |  | Stores the display name of the hierarchy. |
| 9 | `HIERARCHY_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Stores the key of the hierarchy display name. |
| 10 | `HIERARCHY_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | HIERARCHY_NAME_KEY_A_NLS column |
| 11 | `HIERARCHY_NAME_KEY_NLS` | VARCHAR(202) |  |  | Stores the key of the hierarchy display name. |
| 12 | `PRODUCT_TYPE_CD` | DOUBLE | NOT NULL |  | Product (i.e. General Laboratory, Microbiology, ¿) associated with this hierarchy. Code set 28961. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PCS_HIERARCHY_QUEUE_RELTN](PCS_HIERARCHY_QUEUE_RELTN.md) | `HIERARCHY_ID` |
| [PCS_REVIEW_CRITERIA](PCS_REVIEW_CRITERIA.md) | `HIERARCHY_ID` |
| [PCS_REVIEW_ITEM](PCS_REVIEW_ITEM.md) | `HIERARCHY_ID` |

