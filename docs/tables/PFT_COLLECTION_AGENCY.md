# PFT_COLLECTION_AGENCY

> ProFit Collection Agency Table

**Description:** PFT COLLECTION AGENCY  
**Table type:** REFERENCE  
**Primary key:** `PFT_COLLECTION_AGENCY_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGENCY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of agency |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Billing Entity table |
| 8 | `CLIENT_NUMBER` | VARCHAR(20) |  |  | The reference that the collection/precollection agency assigns to the billing entity |
| 9 | `COLLECTION_PERCENTAGE` | DOUBLE |  |  | Collection Percentage amount |
| 10 | `DEFAULT_IND` | DOUBLE |  |  | Indicates if this is the default collection agency |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EXCLUDE_OUTBOUND_INTERFACE_IND` | DOUBLE | NOT NULL |  | Indicates if encounters associated to this collections agency or precollections agency for the given billing entity should be excluded from the outbound interface operations job. True(1) indicates the encounters should be excluded. False(0) indicates encounters should be included. |
| 13 | `INFO_SEND_FLAG` | DOUBLE | NOT NULL |  | Info send |
| 14 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Media type code from code set |
| 15 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Organization table |
| 16 | `PFT_COLLECTION_AGENCY_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 17 | `SELECTED_TASK_ID` | DOUBLE | NOT NULL |  | Stores the queue that the user selected to use |
| 18 | `SEQUENCE` | DOUBLE |  |  | Sequence of the collection agencies |
| 19 | `THIRD_SELF_FLAG` | DOUBLE | NOT NULL |  | Third party or Self pay |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `WRITE_OFF_IND` | DOUBLE |  |  | Indicates write offs |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_CA_CRITERIA_VALUE](PFT_CA_CRITERIA_VALUE.md) | `PFT_COLLECTION_AGENCY_ID` |

